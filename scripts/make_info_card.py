import os
from xml.sax.saxutils import escape
rows = [("Now", "LLM evaluation + benchmark design, Handshake AI", "#7ee787"),
        ("Studying", "CS (ML & Data Science), Univ. of Indianapolis", "#79c0ff"),
        ("Builds", "local-first AI tools; I report where each fails", "#d2a8ff"),
        ("Stack", "Python · PyTorch · TypeScript · Rust · FastAPI", "#ffa657"),
        ("Highlights", "same · llm-ladder · Cutroom · VisaRadar · homeground", "#ff7b72"),
        ("Open to", "Summer 2027 internships", "#7ee787")]
W, H, st = 600, 60 + len(rows) * 34, os.environ.get("STATIC")
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,Menlo,monospace" font-size="13">',
     '<style>.l{opacity:0;animation:i .4s ease-out forwards}@keyframes i{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}</style>',
     f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/><circle cx="20" cy="18" r="5" fill="#ff5f56"/><circle cx="38" cy="18" r="5" fill="#ffbd2e"/><circle cx="56" cy="18" r="5" fill="#27c93f"/>',
     '<text x="80" y="22" fill="#8b949e">parth@github ~ $ neofetch</text>']
for i, (k, v, c) in enumerate(rows):
    y = 62 + i * 34; d = "" if st else f' class="l" style="animation-delay:{0.3+i*0.25:.2f}s"'
    o.append(f'<g{d}><text x="24" y="{y}" fill="{c}" font-weight="bold">{escape(k)}</text><text x="130" y="{y}" fill="#c9d1d9">{escape(v)}</text></g>')
o.append("</svg>"); open("info-card.svg", "w").write("\n".join(o))
