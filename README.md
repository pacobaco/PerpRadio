# PerpRadio

Perpetual internet radio automation: generate tracks from multiple AI music APIs, rotate an MP3 library, rebuild M3U playlists, and host the result. Stripe billing, AzuraCast/Icecast integration, and an optional Tor onion listener are included as scaffolding.

## Pipeline

`originals/ → providers → station/media/*.mp3 → station/playlist.m3u → nginx / Icecast / AzuraCast → Stripe`

An M3U containing file URLs is a playlist, not a live station. For a continuous radio mount, use AutoDJ such as AzuraCast/Liquidsoap with Icecast.

## Features

- Weighted provider rotation: Suno, ElevenLabs, Lyria, Stable Audio
- MP3 library pruning to `max_tracks`
- Clearnet and optional onion M3U playlists
- Stripe plan/meter usage hooks
- Optional AzuraCast upload/start/stop helpers
- nginx/systemd/Tor deployment examples
- Provider adapters designed to be replaced when vendor APIs change

## Requirements

- Python 3.11+
- VPS for public hosting
- API keys for enabled providers
- Stripe keys if selling station hosting
- Owned source audio for cover/audio-to-audio workflows

Suno does not provide an official public API. The Suno adapter targets a configurable unofficial/reseller API shape via `SUNO_API_BASE`; verify the vendor's current API and terms before use.

## Quick start

```bash
cd /opt/perpradio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
cp config.example.json config.json
mkdir -p originals station/media
python radio.py
```

Billing API:

```bash
python app.py
```

Deployment examples:

- `deploy/perpradio.service`
- `deploy/nginx-perpradio.conf`
- `deploy/torrc`
- `deploy/onion-radio.conf`

## Environment

| Variable | Role |
|---|---|
| `SUNO_API_KEY` / `SUNO_API_BASE` | Unofficial/reseller Suno adapter |
| `ELEVENLABS_API_KEY` | Eleven Music |
| `GEMINI_API_KEY` | Lyria through Gemini |
| `STABILITY_API_KEY` | Stable Audio |
| `STRIPE_SECRET_KEY` / `STRIPE_WEBHOOK_SECRET` | Hosting checkout/webhooks |
| `STRIPE_CUSTOMER_ID` / `HOST_PLAN` | Meter destination/plan |
| `AZURACAST_BASE` / `AZURACAST_API_KEY` / `AZURACAST_STATION_ID` | Optional AutoDJ |
| `PUBLIC_BASE_URL` | URL prefix written to M3U |

Only providers with configured credentials are eligible for rotation.

## Rights

Use only source audio and generated material you are permitted to broadcast. Commercial rights, watermarks, cover restrictions, API terms, and output licenses vary by provider and plan. Broadcasting an unlicensed catalog remains potentially infringing regardless of whether the listener connects over clearnet or Tor.

## Operations

```bash
sudo systemctl enable --now perpradio
```

Run `app.py` behind HTTPS nginx for Stripe endpoints. Do not expose billing/admin endpoints on the onion vhost.

## License / status

Scaffolding for self-hosted radio automation. Provider APIs can change without notice. You are responsible for API terms, copyright, licensing, billing configuration, and stream content.
