import os, time
from pathlib import Path
import requests

def generate(root: Path):
    base = os.environ["SUNO_API_BASE"].rstrip("/")
    key = os.environ["SUNO_API_KEY"]
    # Adjust endpoint/payload to your authorized Suno API vendor.
    r = requests.post(f"{base}/generate", headers={"Authorization": f"Bearer {key}"}, json={"mode": "music"}, timeout=60)
    r.raise_for_status()
    data = r.json()
    url = data.get("audio_url") or data.get("url")
    if not url:
        raise RuntimeError("Suno adapter expected audio_url/url in response")
    audio = requests.get(url, timeout=120)
    audio.raise_for_status()
    out = root / "station" / "media" / f"suno-{int(time.time())}.mp3"
    out.write_bytes(audio.content)
    return out
