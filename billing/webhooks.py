import os, stripe

def verify_and_parse(payload: bytes, signature: str):
    return stripe.Webhook.construct_event(
        payload, signature, os.environ["STRIPE_WEBHOOK_SECRET"]
    )

HANDLED_EVENTS = {
    "checkout.session.completed",
    "customer.subscription.updated",
    "customer.subscription.deleted",
    "invoice.payment_failed",
}
