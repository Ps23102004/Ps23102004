import json
d = json.load(open("data/contributions.json")); days = d["days"]
PAL = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
S, G, X0, Y0 = 13, 3, 20, 44
weeks = (len(days) + 6) // 7
W = X0 * 2 + weeks * (S + G); H = Y0 + 7 * (S + G) + 46
first = __import__("datetime").date.fromisoformat(days[0]["date"]).weekday()  # Mon=0
off = (first + 1) % 7  # GitHub weeks start Sunday
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,Menlo,monospace">',
       '<style>.b{opacity:0;animation:r .5s ease-out forwards}@keyframes r{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}text{fill:#8b949e;font-size:12px}</style>',
       f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/>',
       f'<text x="{X0}" y="26">{d["user"]}@github ~ $ ./contributions.sh</text>']
for i, day in enumerate(days):
    k = i + off; wk, dow = divmod(k, 7)
    lv = min(day["level"], 4) + (1 if day["level"] >= 4 and day.get("count", 0) > 20 else 0)
    x = X0 + wk * (S + G); y = Y0 + dow * (S + G)
    out.append(f'<rect class="b" style="animation-delay:{(wk+dow)*0.012:.2f}s" x="{x}" y="{y}" width="{S}" height="{S}" rx="3" fill="{PAL[lv]}"/>')
fy = Y0 + 7 * (S + G) + 22
out.append(f'<text x="{X0}" y="{fy}">{d["total"]:,} contributions in the last year · longest streak {d["longest_streak"]}d · current {d["current_streak"]}d</text>')
lx = W - X0 - 6 * (S + 4) - 80
out.append(f'<text x="{lx}" y="{fy}">Less</text>')
for i, c in enumerate(PAL):
    out.append(f'<rect x="{lx+34+i*(S+4)}" y="{fy-11}" width="{S}" height="{S}" rx="3" fill="{c}"/>')
out.append(f'<text x="{lx+34+6*(S+4)+4}" y="{fy}">More</text></svg>')
open("contrib-heatmap.svg", "w").write("\n".join(out)); print("wrote", W, "x", H)
