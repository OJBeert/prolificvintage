#!/usr/bin/env python3
"""Create Stripe Products + Prices + Payment Links for all LP products."""

import json, subprocess, sys, re, time

# Load API key
import os
KEY = os.environ.get("STRIPE_SECRET_KEY", "")
if not KEY:
    print("ERROR: STRIPE_SECRET_KEY not set"); sys.exit(1)

# ── Product list (extracted from index.html) ──────────────────────────────
PRODUCTS = [
  {"id":1,  "name":"BXH GRAPHIC TEE",              "brand":"BOUNTY HUNTER",           "price":6500},
  {"id":2,  "name":"EC LOGO TEE",                  "brand":"LETITRIDE",               "price":3200},
  {"id":3,  "name":"RAGLAN TEE",                   "brand":"APE SHALL NEVER KILL APE","price":4500},
  {"id":4,  "name":"DIGITAL CAMO RAIN JACKET",     "brand":"A BATHING APE",           "price":45000},
  {"id":5,  "name":"DIGITAL CAMO SHIRT JACKET",    "brand":"A BATHING APE",           "price":30000},
  {"id":6,  "name":"LOGO PRINT TEE",               "brand":"FRESH SCREEN",            "price":3500},
  {"id":7,  "name":"VINTAGE GRAPHIC TEE",          "brand":"UNKNOWN",                 "price":2500},
  {"id":8,  "name":"LIGHTNING GRAPHIC TEE",        "brand":"UNDERCOVER",              "price":9500},
  {"id":9,  "name":"VINTAGE PRINT TEE",            "brand":"HANES",                   "price":2200},
  {"id":10, "name":"CHARACTER GRAPHIC TEE",        "brand":"UNDERCOVER",              "price":9800},
  {"id":11, "name":"ALOHA GIRL SWEAT",             "brand":"HYSTERIC GLAMOUR",        "price":23000},
  {"id":12, "name":"BXH PRINT TEE",               "brand":"BOUNTY HUNTER",           "price":6000},
  {"id":13, "name":"GRAPHIC TEE",                 "brand":"HYSTERIC GLAMOUR",        "price":3800},
  {"id":14, "name":"CAMISOLE",                    "brand":"HYSTERIC GLAMOUR",        "price":14000},
  {"id":15, "name":"HGC SWEATSHIRT",              "brand":"HYSTERIC GLAMOUR",        "price":24000},
  {"id":16, "name":"GRAPHIC TEE",                 "brand":"UNDERCOVER",              "price":7500},
  {"id":17, "name":"RAGLAN PULLOVER",             "brand":"HYSTERIC GLAMOUR",        "price":4200},
  {"id":18, "name":"LACE TANK TOP",               "brand":"HYSTERIC GLAMOUR",        "price":4800},
  {"id":19, "name":"EC LOGO TEE",                 "brand":"EMPIRE COMPANY INC.",     "price":3500},
  {"id":20, "name":"GRAPHIC TEE",                 "brand":"BALANCE",                 "price":2800},
  {"id":21, "name":"GRAPHIC TEE",                 "brand":"BALANCE",                 "price":2800},
  {"id":22, "name":"LOGO PRINT TEE",              "brand":"FRESH SCREEN",            "price":3200},
  {"id":23, "name":"LOGO PRINT TEE",              "brand":"FRESH SCREEN",            "price":3000},
  {"id":24, "name":"LOGO PRINT TEE",              "brand":"FRESH SCREEN",            "price":3200},
  {"id":25, "name":"VINTAGE TEE",                 "brand":"UNITED SPORTS",           "price":2500},
  {"id":26, "name":"PRINT TEE",                   "brand":"FRUIT OF THE LOOM",       "price":2200},
  {"id":27, "name":"OVERSIZED GRAPHIC TEE",       "brand":"CHAOTIC DISCORE",         "price":3500},
  {"id":28, "name":"LACE TANK TOP",               "brand":"HYSTERIC GLAMOUR",        "price":4500},
  {"id":29, "name":"BUTTERFLY GIRL T-SHIRT",      "brand":"HYSTERIC GLAMOUR",        "price":20000},
  {"id":30, "name":"LOGO PULLOVER",               "brand":"HYSTERIC GLAMOUR",        "price":3800},
  {"id":31, "name":"RAGLAN TEE",                  "brand":"HYSTERIC GLAMOUR",        "price":4200},
  {"id":32, "name":"JONIO JACKET",                "brand":"A BATHING APE",           "price":42000},
  {"id":33, "name":"GRAPHIC TEE",                 "brand":"UNDERCOVER",              "price":7200},
]

def stripe_post(endpoint, data):
    cmd = ["curl", "-s", "-X", "POST",
           f"https://api.stripe.com/v1/{endpoint}",
           "-u", f"{KEY}:",
           "--data-urlencode", ""] + []
    # Build form data args
    args = ["curl", "-s", "-X", "POST",
            f"https://api.stripe.com/v1/{endpoint}",
            "-u", f"{KEY}:"]
    for k, v in data.items():
        args += ["-d", f"{k}={v}"]
    r = subprocess.run(args, capture_output=True, text=True)
    return json.loads(r.stdout)

results = []  # {id, name, link_url, error}
errors = []

print(f"Processing {len(PRODUCTS)} products...\n")

for p in PRODUCTS:
    full_name = f"{p['brand']} {p['name']}"
    pid = p["id"]
    print(f"[{pid:02d}/{len(PRODUCTS)}] {full_name} ¥{p['price']:,}", end=" ... ", flush=True)

    try:
        # 1. Create Product
        prod = stripe_post("products", {
            "name": full_name,
            "metadata[lp_id]": str(pid),
        })
        if "error" in prod:
            raise Exception(prod["error"]["message"])
        prod_id = prod["id"]

        # 2. Create Price (JPY, one-time)
        price = stripe_post("prices", {
            "product": prod_id,
            "unit_amount": str(p["price"]),
            "currency": "jpy",
        })
        if "error" in price:
            raise Exception(price["error"]["message"])
        price_id = price["id"]

        # 3. Create Payment Link (qty=1, adjust_quantity=false)
        link = stripe_post("payment_links", {
            "line_items[0][price]": price_id,
            "line_items[0][quantity]": "1",
            "line_items[0][adjustable_quantity][enabled]": "false",
            "after_completion[type]": "redirect",
            "after_completion[redirect][url]": "https://prolific-vintage.pages.dev/thanks",
        })
        if "error" in link:
            raise Exception(link["error"]["message"])

        link_url = link["url"]
        link_id  = link["id"]
        results.append({"id": pid, "name": full_name, "link_url": link_url, "link_id": link_id})
        print(f"✓  {link_url}")

    except Exception as e:
        msg = str(e)
        errors.append({"id": pid, "name": full_name, "error": msg})
        print(f"✗  {msg}")

    time.sleep(0.25)  # rate limit safety

# Write results JSON
out_path = "/Users/ojbeert/lp-system/stripe_links.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\n{'='*60}")
print(f"✓ 成功: {len(results)}/{len(PRODUCTS)} 件")
print(f"✗ エラー: {len(errors)} 件")
if errors:
    for e in errors:
        print(f"  [{e['id']}] {e['name']}: {e['error']}")
print(f"\nリンク一覧: {out_path}")
