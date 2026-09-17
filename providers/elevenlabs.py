import os, time
from pathlib import Path
import requests

def generate(root: Path):
    url = "https://api.elevenlabs.io/v1/music"
    r = requests.post(url, headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"]},
                      json={"prompt": "instrumental radio track", "music_length_ms": 120000}, timeout=120)
    r.raise_for_status()
    out = root / "station" / "media" / f"elevenlabs-{int(time.time())}.mp3"
    out.write_bytes(r.content)
    return out
