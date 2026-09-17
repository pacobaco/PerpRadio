from pathlib import Path
from . import suno, elevenlabs, lyria, stable_audio

def generate(name: str, root: Path):
    return {
        "suno": suno.generate,
        "elevenlabs": elevenlabs.generate,
        "lyria": lyria.generate,
        "stable_audio": stable_audio.generate,
    }[name](root)
