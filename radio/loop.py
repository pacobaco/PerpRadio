import os

def enabled_providers():
    checks = {
        "suno": os.getenv("SUNO_API_KEY"),
        "elevenlabs": os.getenv("ELEVENLABS_API_KEY"),
        "lyria": os.getenv("GEMINI_API_KEY"),
        "stable_audio": os.getenv("STABILITY_API_KEY"),
    }
    return [name for name, key in checks.items() if key]
