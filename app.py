import os
from fastapi import FastAPI, Request, HTTPException
from billing.webhooks import verify_and_parse, HANDLED_EVENTS

app = FastAPI(title="PerpRadio Billing")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("stripe-signature")
    if not signature:
        raise HTTPException(400, "Missing Stripe signature")
    try:
        event = verify_and_parse(payload, signature)
    except Exception:
        raise HTTPException(400, "Invalid webhook")
    if event["type"] in HANDLED_EVENTS:
        # Persist entitlement/subscription state here.
        pass
    return {"received": True}
