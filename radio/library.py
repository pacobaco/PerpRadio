from pathlib import Path

def prune_library(media: Path, max_tracks: int):
    tracks = sorted(media.glob("*.mp3"), key=lambda p: p.stat().st_mtime, reverse=True)
    for old in tracks[max_tracks:]:
        old.unlink(missing_ok=True)

def rebuild_playlist(media: Path, playlist: Path, public_base_url: str):
    tracks = sorted(media.glob("*.mp3"))
    lines = ["#EXTM3U"]
    for track in tracks:
        lines += [f"#EXTINF:-1,{track.stem}", f"{public_base_url}/{track.name}"]
    playlist.parent.mkdir(parents=True, exist_ok=True)
    playlist.write_text("\n".join(lines) + "\n", encoding="utf-8")
