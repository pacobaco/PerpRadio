PLAN_CAPS = {
    "starter": {"suno_covers": 20, "eleven_minutes": 30, "lyria_songs": 20, "stable_gens": 40},
    "pro": {"suno_covers": 200, "eleven_minutes": 200, "lyria_songs": 150, "stable_gens": 200},
}

def cap_for(plan, meter):
    return PLAN_CAPS.get(plan, {}).get(meter)
