#!/usr/bin/env python3
"""
fetch_youtube_transcript.py — Pull a timestamped transcript for a YouTube video.

Why this exists:
  YouTube transcript extraction fails for two very different reasons, and the
  calling model needs to tell them apart:
    (1) NETWORK-BLOCKED  — the execution environment firewalls youtube.com
        (e.g. the Claude.ai sandbox returns x-deny-reason: host_not_allowed).
        No script can fix this. The model must fall back to web search for a
        publisher/show-notes transcript, or ask the user to paste one.
    (2) YOUTUBE-SIDE      — 403/IP throttling, age-gating, or no captions at all.
        Often transient or specific to one video. A second method (yt-dlp) may
        succeed where the first failed.

  This script tries layered methods and, on total failure, prints a single
  machine-readable FALLBACK line so the model knows exactly what to do next.

Usage:
  python fetch_youtube_transcript.py <url-or-id> [--json] [--languages en es ..]
  python fetch_youtube_transcript.py https://youtu.be/zRh0KTutZis
  python fetch_youtube_transcript.py zRh0KTutZis --json > transcript.json

Exit codes:
  0  transcript printed (stdout)
  2  FALLBACK required — could not retrieve; reason printed as FALLBACK:<reason>
  1  usage / unexpected error

Dependencies:
  Required: youtube-transcript-api   (pip install youtube-transcript-api)
  Optional: yt-dlp                   (pip install yt-dlp)  — used as a 2nd method
            and for metadata (title/channel/date) when available.
"""

import argparse
import json
import re
import sys


# ----------------------------- helpers --------------------------------------

def extract_video_id(s: str) -> str:
    """Accept a raw 11-char ID or any common YouTube URL form."""
    s = s.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", s):
        return s
    patterns = [
        r"(?:youtu\.be/)([A-Za-z0-9_-]{11})",
        r"(?:watch\?v=)([A-Za-z0-9_-]{11})",
        r"(?:/shorts/)([A-Za-z0-9_-]{11})",
        r"(?:/embed/)([A-Za-z0-9_-]{11})",
        r"(?:/live/)([A-Za-z0-9_-]{11})",
        r"(?:v=)([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, s)
        if m:
            return m.group(1)
    raise ValueError(f"Could not extract a YouTube video ID from: {s!r}")


def hhmmss(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, sec = divmod(rem, 60)
    if h:
        return f"{h:01d}:{m:02d}:{sec:02d}"
    return f"{m:02d}:{sec:02d}"


def classify_block(err: Exception) -> str:
    """
    Classify a failure so the model knows whether retrying is pointless.
      'network'  — environment firewall / DNS / proxy. No method will ever work.
      'access'   — 403/429 from YouTube or the proxy. Could be firewall OR IP
                   throttling; either way, hammering retries won't help.
      ''         — a YouTube-side, possibly video-specific issue; a 2nd method
                   may still succeed.
    """
    msg = str(err).lower()
    network = [
        "host_not_allowed", "name or service not known", "failed to resolve",
        "temporary failure in name resolution", "connection refused",
        "network is unreachable", "no route to host", "proxy",
    ]
    if any(n in msg for n in network):
        return "network"
    access = ["403", "forbidden", "429", "too many requests", "blocked", "throttl"]
    if any(n in msg for n in access):
        return "access"
    return ""


# --------------------------- method 1: api ----------------------------------

def fetch_via_api(video_id: str, languages):
    """youtube-transcript-api (v1.x instance API). Returns (segments, meta)."""
    from youtube_transcript_api import YouTubeTranscriptApi

    api = YouTubeTranscriptApi()
    chosen = None
    source = None

    # Prefer manually-created in a requested language; then generated; then translate.
    try:
        tlist = api.list(video_id)
        manual, generated = [], []
        for t in tlist:
            (generated if t.is_generated else manual).append(t)

        def first_in_langs(items):
            for lang in languages:
                for t in items:
                    if t.language_code == lang or t.language_code.startswith(lang + "-"):
                        return t
            return None

        chosen = first_in_langs(manual)
        source = "manual" if chosen else None
        if not chosen:
            chosen = first_in_langs(generated)
            source = "auto-generated" if chosen else None
        if not chosen and manual:
            chosen, source = manual[0], f"manual ({manual[0].language_code})"
        if not chosen and generated:
            chosen, source = generated[0], f"auto-generated ({generated[0].language_code})"

        if chosen and chosen.language_code.split("-")[0] not in languages:
            try:
                chosen = chosen.translate(languages[0])
                source = f"{source} → translated to {languages[0]}"
            except Exception:
                pass  # keep original language if translation unsupported

        fetched = chosen.fetch() if chosen else None
    except Exception:
        # .list() can fail on some videos even when .fetch() works — try direct.
        fetched = api.fetch(video_id, languages=languages)
        source = "direct fetch"

    if fetched is None:
        raise RuntimeError("No transcript object returned by API.")

    segments = [
        {"start": float(s.start), "duration": float(getattr(s, "duration", 0.0)), "text": s.text}
        for s in fetched
    ]
    return segments, {"method": "youtube-transcript-api", "track": source}


# --------------------------- method 2: yt-dlp -------------------------------

def fetch_via_ytdlp(video_id: str, languages):
    """Fallback using yt-dlp's auto/manual subtitles + metadata. Optional dep."""
    import yt_dlp  # raises ImportError if not installed

    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitarglangs": languages,
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    meta = {
        "method": "yt-dlp",
        "title": info.get("title"),
        "channel": info.get("channel") or info.get("uploader"),
        "upload_date": info.get("upload_date"),
        "duration": info.get("duration"),
    }

    # Find a usable caption track (json3 carries timing).
    subs = info.get("subtitles") or {}
    autos = info.get("automatic_captions") or {}
    track_url, track_label = None, None
    for store, label in ((subs, "manual"), (autos, "auto-generated")):
        for lang in languages:
            for code in (lang,) + tuple(k for k in store if k.startswith(lang)):
                if code in store:
                    for fmt in store[code]:
                        if fmt.get("ext") == "json3":
                            track_url, track_label = fmt["url"], f"{label} ({code})"
                            break
                if track_url:
                    break
            if track_url:
                break
        if track_url:
            break
    if not track_url:
        raise RuntimeError("yt-dlp found no json3 caption track.")

    import urllib.request
    with urllib.request.urlopen(track_url, timeout=30) as r:
        data = json.loads(r.read().decode("utf-8", "replace"))

    segments = []
    for ev in data.get("events", []):
        if "segs" not in ev:
            continue
        text = "".join(seg.get("utf8", "") for seg in ev["segs"]).strip()
        if not text:
            continue
        segments.append({
            "start": ev.get("tStartMs", 0) / 1000.0,
            "duration": ev.get("dDurationMs", 0) / 1000.0,
            "text": text,
        })
    if not segments:
        raise RuntimeError("yt-dlp caption track had no text segments.")
    meta["track"] = track_label
    return segments, meta


# ------------------------------- main ---------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Fetch a YouTube transcript with timestamps.")
    ap.add_argument("video", help="YouTube URL or 11-char video ID")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of formatted text")
    ap.add_argument("--languages", nargs="+", default=["en"],
                    help="Preferred language codes in priority order (default: en)")
    args = ap.parse_args()

    try:
        video_id = extract_video_id(args.video)
    except ValueError as e:
        print(f"FALLBACK: bad-input — {e}", file=sys.stderr)
        sys.exit(2)

    errors = []
    segments = meta = None

    for method in (fetch_via_api, fetch_via_ytdlp):
        try:
            segments, meta = method(video_id, args.languages)
            if segments:
                break
        except ImportError:
            errors.append(f"{method.__name__}: not installed (optional)")
            continue
        except Exception as e:
            kind = classify_block(e)
            if kind == "network":
                print(
                    "FALLBACK: network-blocked — youtube.com is unreachable from this "
                    "environment (firewall/proxy). No script will work here; do NOT "
                    "retry. Use web search to find a publisher/show-notes transcript or "
                    "a re-uploaded version, or ask the user to paste a transcript.",
                    file=sys.stderr,
                )
                sys.exit(2)
            if kind == "access":
                print(
                    "FALLBACK: access-blocked — YouTube returned 403/429 (environment "
                    "firewall or IP throttling). Retrying the script will not help. Use "
                    "web search for a published transcript or a re-upload, or ask the "
                    "user to paste a transcript.",
                    file=sys.stderr,
                )
                sys.exit(2)
            errors.append(f"{method.__name__}: {type(e).__name__}: {str(e)[:200]}")
            continue

    if not segments:
        reason = " | ".join(errors) or "unknown"
        print(
            f"FALLBACK: no-transcript — every method failed ({reason}). "
            "The video may have captions disabled or be region/age-restricted. "
            "Use web search for a published transcript or a re-upload, or ask the "
            "user to paste one.",
            file=sys.stderr,
        )
        sys.exit(2)

    if args.json:
        out = {"video_id": video_id, "meta": meta, "segments": segments}
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        title = (meta or {}).get("title")
        channel = (meta or {}).get("channel")
        track = (meta or {}).get("track")
        method = (meta or {}).get("method")
        header = [f"# Transcript for video {video_id}"]
        if title:
            header.append(f"# Title: {title}")
        if channel:
            header.append(f"# Channel: {channel}")
        header.append(f"# Source: {method} — {track}")
        header.append("")
        print("\n".join(header))
        for s in segments:
            print(f"[{hhmmss(s['start'])}] {s['text']}")

    # Loud reminder so the calling model always discloses the source in its report.
    print(f"\n# TRANSCRIPT_SOURCE: {meta.get('method')} ({meta.get('track')})", file=sys.stderr)


if __name__ == "__main__":
    main()
