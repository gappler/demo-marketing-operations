"""
Generate 12 months of historical marketing data for Yowie.

Period: April 2025 – March 2026 (12 months leading up to current date April 2026)
Product: Basecamp 45L Pack, $385
Email list as of March 2026: ~4,200 subscribers

Seasonal model for premium outdoor gear:
- Peak: June–September (summer trip planning and execution)
- Secondary peak: October (fall trips, early holiday gifting)
- Low: December–February (winter lull)
- Ramp: March–May (spring planning)

All datasets share a common seasonal index to ensure correlation.
"""

import csv
import os
import random

random.seed(42)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Seasonal model ---
# Months: Apr 2025 (index 0) through Mar 2026 (index 11)
MONTHS = [
    "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09",
    "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03"
]
MONTH_LABELS = [
    "Apr 2025", "May 2025", "Jun 2025", "Jul 2025", "Aug 2025", "Sep 2025",
    "Oct 2025", "Nov 2025", "Dec 2025", "Jan 2026", "Feb 2026", "Mar 2026"
]

# Seasonal multipliers (1.0 = baseline)
SEASONAL = [0.85, 1.00, 1.25, 1.40, 1.35, 1.20, 1.10, 0.75, 0.60, 0.55, 0.65, 0.90]

def jitter(value, pct=0.05):
    """Add small random noise to a value."""
    return round(value * (1 + random.uniform(-pct, pct)))

def jitter_float(value, pct=0.05):
    return round(value * (1 + random.uniform(-pct, pct)), 2)

PRICE = 385
COGS_PER_UNIT = 142  # ~37% COGS for premium DTC

# --- 1. Web Traffic by Source ---
def generate_web_traffic():
    """
    Sources: organic_search, direct, paid_social, email, referral
    Base monthly sessions ~8,000 at seasonal 1.0
    """
    rows = []
    base_total = 8000
    source_split = {
        "organic_search": 0.35,
        "direct": 0.22,
        "paid_social": 0.25,
        "email": 0.10,
        "referral": 0.08,
    }
    for i, month in enumerate(MONTHS):
        s = SEASONAL[i]
        total = jitter(base_total * s, 0.06)
        for source, share in source_split.items():
            sessions = jitter(total * share, 0.08)
            # Bounce rate: paid social higher, email lower
            bounce_base = {"organic_search": 0.52, "direct": 0.38, "paid_social": 0.62, "email": 0.34, "referral": 0.48}
            bounce = round(bounce_base[source] + random.uniform(-0.04, 0.04), 2)
            pages_per = round(random.uniform(2.0, 4.5) if source != "paid_social" else random.uniform(1.5, 2.8), 1)
            avg_duration = round(random.uniform(90, 210) if source in ("direct", "email", "organic_search") else random.uniform(40, 100))
            rows.append([month, source, sessions, bounce, pages_per, avg_duration])

    with open(os.path.join(OUTPUT_DIR, "web_traffic.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "source", "sessions", "bounce_rate", "pages_per_session", "avg_session_duration_sec"])
        w.writerows(rows)
    return rows

# --- 2. Email Campaign Performance ---
def generate_email():
    """
    ~2 campaigns per month. List grows from ~2,800 to ~4,200 over 12 months.
    """
    rows = []
    list_size = 2800
    campaign_types = [
        ("product_feature", "Product feature spotlight"),
        ("story", "Brand story / founder note"),
        ("seasonal", "Seasonal content"),
        ("promotion", "Promotion or offer"),
        ("educational", "Trail / gear education"),
    ]
    campaign_num = 0
    for i, month in enumerate(MONTHS):
        s = SEASONAL[i]
        # 2 campaigns per month, occasionally 3 in peak
        num_campaigns = 3 if s >= 1.25 and random.random() > 0.5 else 2
        monthly_growth = jitter(int(120 * s), 0.15)

        for c in range(num_campaigns):
            campaign_num += 1
            ctype, cdesc = random.choice(campaign_types)
            sent = jitter(int(list_size * 0.95), 0.02)  # 95% deliverability
            # Open rates: 28-42% for this audience (older, engaged, small list)
            open_rate = jitter_float(0.35 * (1 + (s - 1) * 0.15), 0.08)
            open_rate = min(open_rate, 0.48)
            opens = int(sent * open_rate)
            # CTR: 3.5-6% of opens
            ctr = jitter_float(0.045, 0.15)
            clicks = max(int(opens * ctr), 1)
            # Unsubs: 0.1-0.3%
            unsubs = max(int(sent * random.uniform(0.001, 0.003)), 0)
            # Conversions: 1.5-4% of clicks
            conv_rate = random.uniform(0.015, 0.04) * s
            conversions = max(int(clicks * conv_rate), 0)
            revenue = conversions * PRICE

            rows.append([
                month,
                f"YW-EM-{campaign_num:03d}",
                ctype,
                list_size,
                sent,
                opens,
                open_rate,
                clicks,
                ctr,
                conversions,
                revenue,
                unsubs,
            ])
            list_size -= unsubs

        list_size += monthly_growth
        list_size = min(list_size, 4250)

    with open(os.path.join(OUTPUT_DIR, "email_campaigns.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "month", "campaign_id", "campaign_type", "list_size", "sent",
            "opens", "open_rate", "clicks", "click_through_rate",
            "conversions", "revenue", "unsubscribes"
        ])
        w.writerows(rows)
    return rows

# --- 3. Meta Ad Spend and Results ---
def generate_meta_ads():
    """
    Monthly Meta ad budget scales with season. Base ~$2,500/mo.
    """
    rows = []
    base_spend = 2500
    for i, month in enumerate(MONTHS):
        s = SEASONAL[i]
        spend = jitter(int(base_spend * s), 0.08)
        # CPM: $18-28 range, higher in peak
        cpm = jitter_float(22 + (s - 1) * 8, 0.06)
        impressions = int((spend / cpm) * 1000)
        # CTR: 0.8-1.4%
        ctr = jitter_float(0.011 * (1 + (s - 1) * 0.2), 0.10)
        clicks = int(impressions * ctr)
        cpc = round(spend / max(clicks, 1), 2)
        # Landing page conversion: 2.5-4.2%
        lp_conv_rate = jitter_float(0.032 * s, 0.12)
        lp_conv_rate = max(lp_conv_rate, 0.018)
        conversions = max(int(clicks * lp_conv_rate), 0)
        revenue = conversions * PRICE
        roas = round(revenue / spend, 2) if spend > 0 else 0
        # Add to cart but didn't buy
        add_to_cart = conversions + jitter(int(conversions * 1.8), 0.2)

        rows.append([
            month, spend, impressions, clicks, ctr, cpc, cpm,
            add_to_cart, conversions, revenue, roas
        ])

    with open(os.path.join(OUTPUT_DIR, "meta_ads.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "month", "spend", "impressions", "clicks", "ctr", "cpc", "cpm",
            "add_to_cart", "conversions", "revenue", "roas"
        ])
        w.writerows(rows)
    return rows

# --- 4. Social Media Engagement ---
def generate_social():
    """
    Organic social: Instagram + Facebook. Small but engaged following.
    """
    rows = []
    ig_followers = 3200
    fb_followers = 1850

    for i, month in enumerate(MONTHS):
        s = SEASONAL[i]
        # Instagram
        ig_posts = random.choice([8, 10, 12]) if s >= 1.0 else random.choice([6, 8])
        ig_reach = jitter(int(ig_followers * 2.2 * s), 0.10)
        ig_impressions = jitter(int(ig_reach * 1.6), 0.08)
        ig_engagement_rate = jitter_float(0.038 * (1 + (s - 1) * 0.3), 0.10)
        ig_engagements = int(ig_impressions * ig_engagement_rate)
        ig_follower_growth = jitter(int(85 * s), 0.15)
        ig_followers += ig_follower_growth
        ig_profile_visits = jitter(int(ig_followers * 0.12 * s), 0.10)
        ig_link_clicks = jitter(int(ig_profile_visits * 0.18), 0.12)

        rows.append([
            month, "instagram", ig_followers, ig_posts, ig_reach, ig_impressions,
            ig_engagements, ig_engagement_rate, ig_follower_growth, ig_profile_visits, ig_link_clicks
        ])

        # Facebook
        fb_posts = random.choice([6, 8])
        fb_reach = jitter(int(fb_followers * 1.4 * s), 0.10)
        fb_impressions = jitter(int(fb_reach * 1.8), 0.08)
        fb_engagement_rate = jitter_float(0.022 * (1 + (s - 1) * 0.2), 0.10)
        fb_engagements = int(fb_impressions * fb_engagement_rate)
        fb_follower_growth = jitter(int(40 * s), 0.15)
        fb_followers += fb_follower_growth
        fb_link_clicks = jitter(int(fb_reach * 0.015), 0.12)

        rows.append([
            month, "facebook", fb_followers, fb_posts, fb_reach, fb_impressions,
            fb_engagements, fb_engagement_rate, fb_follower_growth, 0, fb_link_clicks
        ])

    with open(os.path.join(OUTPUT_DIR, "social_media.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "month", "platform", "followers", "posts_published", "reach",
            "impressions", "engagements", "engagement_rate", "follower_growth",
            "profile_visits", "link_clicks"
        ])
        w.writerows(rows)
    return rows

# --- 5. Customer Orders ---
def generate_orders():
    """
    Individual orders. ~40-80/month depending on season.
    Total annual ~720 units — realistic for a small premium DTC brand in year 1-2.
    """
    rows = []
    base_monthly_orders = 55
    regions = ["mountain_west", "northeast", "pacific_northwest", "southeast", "midwest"]
    region_weights = [0.30, 0.28, 0.25, 0.10, 0.07]
    channels = ["paid_social", "organic_search", "email", "direct", "referral"]
    order_id = 10000

    for i, month in enumerate(MONTHS):
        s = SEASONAL[i]
        num_orders = jitter(int(base_monthly_orders * s), 0.08)
        monthly_revenue = 0
        monthly_units = 0

        for _ in range(num_orders):
            order_id += 1
            # Day within month
            day = random.randint(1, 28)
            date = f"{month}-{day:02d}"
            qty = 1 if random.random() < 0.92 else 2  # 8% buy 2
            subtotal = qty * PRICE
            # Discount: 85% pay full price, 10% get 10% off (email promo), 5% get 15% off (referral)
            discount_roll = random.random()
            if discount_roll < 0.85:
                discount = 0
                discount_code = ""
            elif discount_roll < 0.95:
                discount = round(subtotal * 0.10, 2)
                discount_code = "WELCOME10"
            else:
                discount = round(subtotal * 0.15, 2)
                discount_code = "FRIEND15"
            total = round(subtotal - discount, 2)
            # Channel attribution
            channel = random.choices(channels, weights=[0.30, 0.28, 0.18, 0.14, 0.10])[0]
            region = random.choices(regions, weights=region_weights)[0]
            # New vs returning (mostly new for single-product brand, but some gift repeats)
            customer_type = "new" if random.random() < 0.88 else "returning"

            rows.append([
                f"YW-{order_id}",
                date,
                month,
                qty,
                subtotal,
                discount,
                discount_code,
                total,
                channel,
                region,
                customer_type,
            ])
            monthly_revenue += total
            monthly_units += qty

    with open(os.path.join(OUTPUT_DIR, "orders.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "order_id", "order_date", "month", "quantity", "subtotal",
            "discount", "discount_code", "total", "attribution_channel",
            "customer_region", "customer_type"
        ])
        w.writerows(rows)
    return rows

# --- Generate monthly summary ---
def generate_summary(web, email, meta, social, orders):
    """Roll everything up into a single monthly summary."""
    rows = []
    for i, month in enumerate(MONTHS):
        # Web traffic total
        total_sessions = sum(r[2] for r in web if r[0] == month)
        # Email metrics
        email_sent = sum(r[4] for r in email if r[0] == month)
        email_revenue = sum(r[10] for r in email if r[0] == month)
        # Meta
        meta_row = [r for r in meta if r[0] == month][0]
        meta_spend = meta_row[1]
        meta_revenue = meta_row[9]
        meta_roas = meta_row[10]
        # Social
        social_rows = [r for r in social if r[0] == month]
        total_engagements = sum(r[6] for r in social_rows)
        # Orders
        month_orders = [r for r in orders if r[2] == month]
        total_orders = len(month_orders)
        total_units = sum(r[3] for r in month_orders)
        total_revenue = sum(r[7] for r in month_orders)
        avg_order_value = round(total_revenue / max(total_orders, 1), 2)

        rows.append([
            month, total_sessions, email_sent, email_revenue,
            meta_spend, meta_revenue, meta_roas,
            total_engagements, total_orders, total_units,
            total_revenue, avg_order_value
        ])

    with open(os.path.join(OUTPUT_DIR, "monthly_summary.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "month", "web_sessions", "emails_sent", "email_revenue",
            "meta_spend", "meta_revenue", "meta_roas",
            "social_engagements", "orders", "units_sold",
            "total_revenue", "avg_order_value"
        ])
        w.writerows(rows)


if __name__ == "__main__":
    print("Generating Yowie historical data (Apr 2025 – Mar 2026)...")
    web = generate_web_traffic()
    print(f"  web_traffic.csv — {len(web)} rows")
    email = generate_email()
    print(f"  email_campaigns.csv — {len(email)} rows")
    meta = generate_meta_ads()
    print(f"  meta_ads.csv — {len(meta)} rows")
    social = generate_social()
    print(f"  social_media.csv — {len(social)} rows")
    orders = generate_orders()
    print(f"  orders.csv — {len(orders)} rows")
    generate_summary(web, email, meta, social, orders)
    print(f"  monthly_summary.csv — 12 rows")
    print("Done.")
