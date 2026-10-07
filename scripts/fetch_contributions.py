"""Scrape the public contributions calendar (no token). Unofficial endpoint: fail loudly if it changes."""
import json, sys, requests
from bs4 import BeautifulSoup
USER = sys.argv[1] if len(sys.argv) > 1 else "Ps23102004"
html = requests.get(f"https://github.com/users/{USER}/contributions", timeout=30).text
soup = BeautifulSoup(html, "html.parser")
days = []
for td in soup.select("td.ContributionCalendar-day"):
    if td.get("data-date"):
        days.append({"date": td["data-date"], "level": int(td.get("data-level", 0))})
tips = {t.get("for"): t.get_text(" ", strip=True) for t in soup.select("tool-tip")}
for td in soup.select("td.ContributionCalendar-day"):
    t = tips.get(td.get("id"), "")
    n = 0 if t.startswith("No") else int(next((w for w in t.split() if w.isdigit()), 0))
    for d in days:
        if d["date"] == td.get("data-date"):
            d["count"] = n
if len(days) < 300:
    sys.exit(f"parsed only {len(days)} days - endpoint changed? keeping previous data")
days.sort(key=lambda d: d["date"])
total = sum(d.get("count", 0) for d in days)
best = 0; cur = 0
for d in days:
    cur = cur + 1 if d.get("count", 0) else 0; best = max(best, cur)
streak = 0
for d in reversed(days):
    if d.get("count", 0): streak += 1
    elif streak or d is not days[-1]: break
json.dump({"user": USER, "days": days, "total": total, "longest_streak": best, "current_streak": streak}, open("data/contributions.json", "w"))
print(USER, len(days), "days,", total, "contributions")
