"""
Yowie Monthly Marketing Report Generator

Reads CSV data from the data/ folder, analyzes the most recent month
(or a specified month), and outputs a formatted markdown report with
metrics, trends, insights, and recommendations.

Written in Yowie brand voice: plainspoken, confident, restrained, dry.

Usage:
    python tools/generate_monthly_report.py                  # latest month
    python tools/generate_monthly_report.py 2025-07          # specific month
    python tools/generate_monthly_report.py --all            # full year
"""

import csv
import os
import sys
from datetime import datetime

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

MONTH_NAMES = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December",
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def load_all():
    return {
        "summary": load_csv("monthly_summary.csv"),
        "meta": load_csv("meta_ads.csv"),
        "email": load_csv("email_campaigns.csv"),
        "web": load_csv("web_traffic.csv"),
        "social": load_csv("social_media.csv"),
        "orders": load_csv("orders.csv"),
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def fmt_money(v):
    """Format a number as dollars with commas, no cents."""
    return f"${int(round(v)):,}"


def fmt_pct(v):
    """Format a decimal as a percentage string."""
    return f"{v * 100:.1f}%"


def fmt_num(v):
    return f"{int(round(v)):,}"


def delta_pct(current, previous):
    if previous == 0:
        return 0
    return (current - previous) / previous


def delta_str(current, previous):
    d = delta_pct(current, previous)
    sign = "+" if d >= 0 else ""
    return f"{sign}{d * 100:.1f}%"


def month_label(month_key):
    year, mm = month_key.split("-")
    return f"{MONTH_NAMES[mm]} {year}"


def get_row(rows, month):
    return next((r for r in rows if r["month"] == month), None)


def get_rows(rows, month):
    return [r for r in rows if r["month"] == month]


def prev_month(month_key, all_months):
    idx = all_months.index(month_key)
    return all_months[idx - 1] if idx > 0 else None


def f(row, key):
    """Get a float from a CSV row."""
    return float(row[key])


# ---------------------------------------------------------------------------
# Analysis functions
# ---------------------------------------------------------------------------
def analyze_revenue(data, month, prev):
    s = get_row(data["summary"], month)
    revenue = f(s, "total_revenue")
    units = int(f(s, "units_sold"))
    orders = int(f(s, "orders"))
    aov = f(s, "avg_order_value")

    result = {
        "revenue": revenue,
        "units": units,
        "orders": orders,
        "aov": aov,
    }

    if prev:
        sp = get_row(data["summary"], prev)
        result["rev_delta"] = delta_str(revenue, f(sp, "total_revenue"))
        result["units_delta"] = delta_str(units, f(sp, "units_sold"))
        result["aov_delta"] = delta_str(aov, f(sp, "avg_order_value"))
    return result


def analyze_meta(data, month, prev):
    m = get_row(data["meta"], month)
    spend = f(m, "spend")
    rev = f(m, "revenue")
    roas = f(m, "roas")
    clicks = int(f(m, "clicks"))
    conv = int(f(m, "conversions"))
    cpc = f(m, "cpc")
    cpm = f(m, "cpm")
    cac = spend / conv if conv > 0 else 0
    atc = int(f(m, "add_to_cart"))
    atc_to_conv = conv / atc if atc > 0 else 0

    result = {
        "spend": spend, "revenue": rev, "roas": roas,
        "clicks": clicks, "conversions": conv,
        "cpc": cpc, "cpm": cpm, "cac": cac,
        "atc": atc, "atc_to_conv": atc_to_conv,
    }

    if prev:
        mp = get_row(data["meta"], prev)
        result["roas_delta"] = delta_str(roas, f(mp, "roas"))
        result["spend_delta"] = delta_str(spend, f(mp, "spend"))
        result["cac_prev"] = f(mp, "spend") / max(int(f(mp, "conversions")), 1)
    return result


def analyze_email(data, month):
    camps = get_rows(data["email"], month)
    if not camps:
        return None

    total_sent = sum(int(f(c, "sent")) for c in camps)
    total_opens = sum(int(f(c, "opens")) for c in camps)
    total_clicks = sum(int(f(c, "clicks")) for c in camps)
    total_conv = sum(int(f(c, "conversions")) for c in camps)
    total_rev = sum(f(c, "revenue") for c in camps)
    total_unsubs = sum(int(f(c, "unsubscribes")) for c in camps)
    list_size = max(int(f(c, "list_size")) for c in camps)
    avg_open_rate = total_opens / total_sent if total_sent else 0
    avg_ctr = total_clicks / total_opens if total_opens else 0

    best_camp = max(camps, key=lambda c: f(c, "open_rate"))

    return {
        "campaigns": len(camps),
        "sent": total_sent,
        "opens": total_opens,
        "clicks": total_clicks,
        "conversions": total_conv,
        "revenue": total_rev,
        "unsubs": total_unsubs,
        "list_size": list_size,
        "open_rate": avg_open_rate,
        "ctr": avg_ctr,
        "best_campaign": best_camp,
    }


def analyze_web(data, month, prev):
    rows = get_rows(data["web"], month)
    by_source = {r["source"]: int(f(r, "sessions")) for r in rows}
    total = sum(by_source.values())

    result = {"total": total, "by_source": by_source}

    if prev:
        prev_rows = get_rows(data["web"], prev)
        prev_total = sum(int(f(r, "sessions")) for r in prev_rows)
        result["total_delta"] = delta_str(total, prev_total)

    # Best and worst source by share
    sorted_sources = sorted(by_source.items(), key=lambda x: x[1], reverse=True)
    result["top_source"] = sorted_sources[0]
    result["sources_ranked"] = sorted_sources
    return result


def analyze_social(data, month, prev):
    rows = get_rows(data["social"], month)
    result = {}
    for r in rows:
        platform = r["platform"]
        result[platform] = {
            "followers": int(f(r, "followers")),
            "posts": int(f(r, "posts_published")),
            "reach": int(f(r, "reach")),
            "engagements": int(f(r, "engagements")),
            "eng_rate": f(r, "engagement_rate"),
            "growth": int(f(r, "follower_growth")),
            "link_clicks": int(f(r, "link_clicks")),
        }
    return result


def analyze_orders(data, month):
    orders = get_rows(data["orders"], month)
    if not orders:
        return None

    by_region = {}
    by_channel = {}
    new_count = 0
    discount_count = 0

    for o in orders:
        region = o["customer_region"]
        channel = o["attribution_channel"]
        by_region[region] = by_region.get(region, 0) + 1
        by_channel[channel] = by_channel.get(channel, 0) + 1
        if o["customer_type"] == "new":
            new_count += 1
        if float(o["discount"]) > 0:
            discount_count += 1

    return {
        "total": len(orders),
        "by_region": dict(sorted(by_region.items(), key=lambda x: x[1], reverse=True)),
        "by_channel": dict(sorted(by_channel.items(), key=lambda x: x[1], reverse=True)),
        "new_pct": new_count / len(orders) if orders else 0,
        "discount_pct": discount_count / len(orders) if orders else 0,
    }


def compute_ytd(data, through_month):
    all_months = [r["month"] for r in data["summary"]]
    idx = all_months.index(through_month)
    months_so_far = all_months[: idx + 1]

    total_rev = sum(f(r, "total_revenue") for r in data["summary"] if r["month"] in months_so_far)
    total_units = sum(int(f(r, "units_sold")) for r in data["summary"] if r["month"] in months_so_far)
    total_meta_spend = sum(f(r, "spend") for r in data["meta"] if r["month"] in months_so_far)
    total_meta_rev = sum(f(r, "revenue") for r in data["meta"] if r["month"] in months_so_far)

    return {
        "months": len(months_so_far),
        "revenue": total_rev,
        "units": total_units,
        "meta_spend": total_meta_spend,
        "meta_roas": total_meta_rev / total_meta_spend if total_meta_spend else 0,
    }


# ---------------------------------------------------------------------------
# Insight generation
# ---------------------------------------------------------------------------
def generate_insights(rev, meta, email, web, social, orders, ytd):
    """Generate 3-5 insights based on the data. Plainspoken, no fluff."""
    insights = []

    # Revenue trend
    if "rev_delta" in rev:
        d = delta_pct(rev["revenue"], rev["revenue"] / (1 + delta_pct(rev["revenue"], rev["revenue"])))
        if rev["rev_delta"].startswith("+"):
            insights.append(f"Revenue is up {rev['rev_delta']} month-over-month. The seasonal pattern is doing its job.")
        elif rev["rev_delta"].startswith("-"):
            pct = rev["rev_delta"]
            insights.append(f"Revenue dropped {pct} from last month. Expected if we're heading into the off-season. Worth watching if the trend continues into spring.")

    # Meta efficiency
    if meta["roas"] >= 6.0:
        insights.append(f"Meta ROAS hit {meta['roas']}x this month. The spend-to-return ratio is strong — this is where we lean in.")
    elif meta["roas"] < 4.0:
        insights.append(f"Meta ROAS dropped to {meta['roas']}x. Below the 4x floor, the math stops working. Either the creative is tired or we're spending into the wrong season.")

    # CAC movement
    if "cac_prev" in meta and meta["cac"] > 0:
        if meta["cac"] > meta["cac_prev"] * 1.15:
            insights.append(f"CAC climbed to {fmt_money(meta['cac'])} from {fmt_money(meta['cac_prev'])} last month. Acquisition is getting more expensive — check creative fatigue and audience saturation.")
        elif meta["cac"] < meta["cac_prev"] * 0.85:
            insights.append(f"CAC dropped to {fmt_money(meta['cac'])} from {fmt_money(meta['cac_prev'])}. More efficient month. The audience is responding.")

    # Email engagement
    if email:
        if email["open_rate"] >= 0.37:
            insights.append(f"Email open rates are at {fmt_pct(email['open_rate'])}. For a list this size, that's excellent. This audience reads what we send them.")
        elif email["open_rate"] < 0.32:
            insights.append(f"Email open rates slipped to {fmt_pct(email['open_rate'])}. The list is growing, but engagement per subscriber is softening. Quality over quantity.")

    # Add-to-cart drop-off
    if meta["atc"] > 0 and meta["atc_to_conv"] < 0.35:
        drop = (1 - meta["atc_to_conv"]) * 100
        insights.append(f"{int(drop)}% of add-to-carts didn't convert. At $385, some hesitation is normal. But if the cart abandonment rate keeps climbing, we need to look at the checkout flow.")

    # Web traffic composition
    if web:
        organic_share = web["by_source"].get("organic_search", 0) / web["total"]
        paid_share = web["by_source"].get("paid_social", 0) / web["total"]
        if organic_share > paid_share:
            insights.append("Organic search is driving more traffic than paid. That's a good sign for long-term acquisition cost, but it means we're more exposed to algorithm changes.")
        elif paid_share > 0.35:
            insights.append(f"Paid social accounts for {fmt_pct(paid_share)} of traffic. We're dependent on the ad budget for volume. Organic and referral need to carry more weight.")

    return insights[:5]


def generate_recommendations(rev, meta, email, web, social, orders, ytd):
    """Generate 2-4 recommendations. Direct, actionable, no hedging."""
    recs = []

    # Meta budget
    if meta["roas"] >= 5.5:
        recs.append("**Increase Meta spend by 15-20% next month.** ROAS supports it. Test a second creative angle to find the ceiling before it finds us.")
    elif meta["roas"] < 4.0:
        recs.append("**Pull back Meta spend by 20%.** Below 4x ROAS, we're buying conversions at a loss when you factor in COGS and fulfillment. Redirect budget to email and content.")

    # Email
    if email:
        if email["conversions"] == 0:
            recs.append("**Email drove zero conversions this month.** The list is engaged (opens are solid), but nothing in the funnel is converting. Test a product-focused email with a direct CTA — no story, no education, just the pack and a reason to buy now.")
        elif email["open_rate"] < 0.33:
            recs.append("**Revisit email subject lines.** Open rates are below 33%. Test shorter, more direct subjects. This audience doesn't want cleverness — they want relevance.")
        if email["unsubs"] > email["sent"] * 0.003:
            recs.append("**Watch unsubscribe rate.** It's above 0.3% this month. Might be sending too frequently, or the content isn't matching what subscribers signed up for.")

    # Seasonal prep
    all_months = ["2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09",
                  "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03"]
    current_mm = rev.get("_month", "")
    if current_mm in ("2026-02", "2026-03", "2025-02", "2025-03"):
        recs.append("**Spring ramp is starting.** This is the window to refresh creative, build the email pipeline, and prep for the June-August push. Front-load the work now.")
    elif current_mm in ("2025-10", "2025-11", "2026-10", "2026-11"):
        recs.append("**Seasonal slowdown ahead.** Shift budget from acquisition to retention. Focus on post-purchase emails, warranty registration nudges, and referral program activation.")

    # Orders
    if orders and orders["new_pct"] > 0.90:
        recs.append("**92%+ of orders are new customers.** That's expected for a single-SKU brand, but explore repeat triggers: gift purchases, warranty registration follow-ups, or a care/repair kit add-on down the line.")

    return recs[:4]


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(data, month):
    all_months = [r["month"] for r in data["summary"]]
    prev = prev_month(month, all_months)

    rev = analyze_revenue(data, month, prev)
    rev["_month"] = month
    meta = analyze_meta(data, month, prev)
    email = analyze_email(data, month)
    web = analyze_web(data, month, prev)
    social = analyze_social(data, month, prev)
    orders = analyze_orders(data, month)
    ytd = compute_ytd(data, month)

    insights = generate_insights(rev, meta, email, web, social, orders, ytd)
    recs = generate_recommendations(rev, meta, email, web, social, orders, ytd)

    label = month_label(month)
    year, mm = month.split("-")

    # --- Build the report ---
    lines = []
    w = lines.append

    w("---")
    w(f"title: Yowie Monthly Marketing Report — {label}")
    w("type: monthly_report")
    w("version: 1.0")
    w(f"generated: {datetime.now().strftime('%Y-%m-%d')}")
    w(f"period: {month}")
    w(f"product: Basecamp 45L Pack")
    w(f"price: $385")
    w("---")
    w("")
    w(f"# {label} — Marketing Report")
    w("")

    # --- Summary ---
    w("## The Month in Brief")
    w("")

    prev_label = month_label(prev) if prev else None
    rev_context = f", {rev.get('rev_delta', '')} from {prev_label}" if prev else ""
    w(f"{fmt_money(rev['revenue'])} in revenue{rev_context}. "
      f"{fmt_num(rev['units'])} units moved at an average order value of {fmt_money(rev['aov'])}. "
      f"Meta returned {meta['roas']}x on {fmt_money(meta['spend'])} in spend.")
    w("")

    # --- Key Metrics Table ---
    w("## Key Metrics")
    w("")
    w("| Metric | This Month | vs. Prior |")
    w("|--------|-----------|-----------|")
    w(f"| Revenue | {fmt_money(rev['revenue'])} | {rev.get('rev_delta', '—')} |")
    w(f"| Units Sold | {fmt_num(rev['units'])} | {rev.get('units_delta', '—')} |")
    w(f"| Orders | {fmt_num(rev['orders'])} | — |")
    w(f"| Avg Order Value | {fmt_money(rev['aov'])} | {rev.get('aov_delta', '—')} |")
    w(f"| Meta Ad Spend | {fmt_money(meta['spend'])} | {meta.get('spend_delta', '—')} |")
    w(f"| Meta ROAS | {meta['roas']}x | {meta.get('roas_delta', '—')} |")
    w(f"| Meta CAC | {fmt_money(meta['cac'])} | — |")
    w(f"| Web Sessions | {fmt_num(web['total'])} | {web.get('total_delta', '—')} |")
    if email:
        w(f"| Email Open Rate | {fmt_pct(email['open_rate'])} | — |")
        w(f"| Email List Size | {fmt_num(email['list_size'])} | — |")
    w("")

    # --- Channel Performance ---
    w("## Channel Performance")
    w("")
    w("### Meta Ads")
    w("")
    w(f"Spent {fmt_money(meta['spend'])} and brought in {fmt_money(meta['revenue'])} "
      f"at {meta['roas']}x ROAS. {fmt_num(meta['clicks'])} clicks at "
      f"${meta['cpc']:.2f} CPC, {meta['conversions']} conversions. "
      f"{meta['atc']} added to cart, {meta['conversions']} completed checkout "
      f"({fmt_pct(meta['atc_to_conv'])} cart completion rate).")
    w("")

    if email:
        w("### Email")
        w("")
        w(f"Sent {email['campaigns']} campaigns to a list of {fmt_num(email['list_size'])}. "
          f"Average open rate: {fmt_pct(email['open_rate'])}. "
          f"{email['clicks']} total clicks, {email['conversions']} conversions "
          f"for {fmt_money(email['revenue'])} in email-attributed revenue. "
          f"{email['unsubs']} unsubscribes.")
        w("")
        best = email["best_campaign"]
        w(f"Best performer: **{best['campaign_id']}** ({best['campaign_type'].replace('_', ' ')}) "
          f"— {fmt_pct(float(best['open_rate']))} open rate.")
        w("")

    w("### Web Traffic")
    w("")
    w(f"{fmt_num(web['total'])} sessions{' (' + web.get('total_delta', '') + ' MoM)' if web.get('total_delta') else ''}.")
    w("")
    w("| Source | Sessions | Share |")
    w("|--------|----------|-------|")
    for source, sessions in web["sources_ranked"]:
        share = sessions / web["total"]
        label_clean = source.replace("_", " ").title()
        w(f"| {label_clean} | {fmt_num(sessions)} | {fmt_pct(share)} |")
    w("")

    w("### Social")
    w("")
    for platform, d in social.items():
        name = platform.title()
        w(f"**{name}:** {fmt_num(d['followers'])} followers (+{d['growth']}). "
          f"{d['posts']} posts, {fmt_num(d['reach'])} reach, "
          f"{fmt_num(d['engagements'])} engagements ({fmt_pct(d['eng_rate'])}). "
          f"{d['link_clicks']} link clicks.")
        w("")

    # --- Orders Breakdown ---
    if orders:
        w("## Order Breakdown")
        w("")
        w(f"{orders['total']} orders. {fmt_pct(orders['new_pct'])} new customers, "
          f"{fmt_pct(orders['discount_pct'])} used a discount code.")
        w("")

        w("**By Region:**")
        w("")
        for region, count in orders["by_region"].items():
            region_label = region.replace("_", " ").title()
            w(f"- {region_label}: {count} ({fmt_pct(count / orders['total'])})")
        w("")

        w("**By Channel:**")
        w("")
        for channel, count in orders["by_channel"].items():
            channel_label = channel.replace("_", " ").title()
            w(f"- {channel_label}: {count} ({fmt_pct(count / orders['total'])})")
        w("")

    # --- Year-to-Date ---
    w("## Year to Date")
    w("")
    w(f"Through {month_label(month)} ({ytd['months']} months): "
      f"{fmt_money(ytd['revenue'])} total revenue, {fmt_num(ytd['units'])} units sold, "
      f"{ytd['meta_roas']:.1f}x blended Meta ROAS on {fmt_money(ytd['meta_spend'])} in ad spend.")
    w("")

    # --- Insights ---
    w("## What We Noticed")
    w("")
    for insight in insights:
        w(f"- {insight}")
    w("")

    # --- Recommendations ---
    w("## What to Do About It")
    w("")
    for rec in recs:
        w(f"- {rec}")
    w("")

    # --- Footer ---
    w("---")
    w("")
    w(f"*Report generated {datetime.now().strftime('%Y-%m-%d')}. "
      f"Data source: Yowie marketing simulation. "
      f"Product: Basecamp 45L Pack, $385.*")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    data = load_all()
    all_months = [r["month"] for r in data["summary"]]

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--all":
            months = all_months
        elif arg in all_months:
            months = [arg]
        else:
            print(f"Unknown month: {arg}")
            print(f"Available: {', '.join(all_months)}")
            sys.exit(1)
    else:
        months = [all_months[-1]]

    for month in months:
        report = generate_report(data, month)
        year, mm = month.split("-")
        filename = f"report_{year}_{mm}.md"
        outpath = os.path.join(DOCS_DIR, filename)
        with open(outpath, "w") as out:
            out.write(report)
        print(f"  {filename} — {month_label(month)}")

    print(f"\nDone. {len(months)} report(s) written to docs/")


if __name__ == "__main__":
    main()
