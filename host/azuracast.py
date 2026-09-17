import os, requests

def upload_file(path):
    base = os.environ["AZURACAST_BASE"].rstrip("/")
    station = os.environ["AZURACAST_STATION_ID"]
    key = os.environ["AZURACAST_API_KEY"]
    with open(path, "rb") as f:
        r = requests.post(f"{base}/api/station/{station}/files", headers={"X-API-Key": key},
                          files={"file": f}, timeout=120)
    r.raise_for_status()
    return r.json()

def station_action(action):
    base = os.environ["AZURACAST_BASE"].rstrip("/")
    station = os.environ["AZURACAST_STATION_ID"]
    key = os.environ["AZURACAST_API_KEY"]
    r = requests.post(f"{base}/api/station/{station}/backend/{action}",
                      headers={"X-API-Key": key}, timeout=30)
    r.raise_for_status()
    return r.json()
