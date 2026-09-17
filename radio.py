import json, os, random, time
from pathlib import Path
from dotenv import load_dotenv

from radio.library import prune_library, rebuild_playlist
from radio.loop import enabled_providers
from providers import generate

load_dotenv()

ROOT = Path(__file__).parent
CONFIG = json.loads((ROOT / "config.json").read_text()) if (ROOT / "config.json").exists() else json.loads((ROOT / "config.example.json").read_text())
MEDIA = ROOT / "station" / "media"
MEDIA.mkdir(parents=True, exist_ok=True)

def pick_provider(names, weights):
    return random.choices(names, weights=[weights.get(n, 1) for n in names], k=1)[0]

def cycle():
    names = enabled_providers()
    if not names:
        print("No providers configured; waiting.")
        return
    provider = pick_provider(names, CONFIG.get("weights", {}))
    try:
        output = generate(provider, ROOT)
        print(f"generated: {output}")
    except Exception as exc:
        print(f"{provider} failed: {exc}")
        return
    prune_library(MEDIA, CONFIG.get("max_tracks", 200))
    rebuild_playlist(
        MEDIA,
        ROOT / "station" / "playlist.m3u",
        CONFIG.get("public_base_url", "").rstrip("/"),
    )

if __name__ == "__main__":
    while True:
        cycle()
        time.sleep(CONFIG.get("generate_every_minutes", 25) * 60)
