"""Convert emblem-source.png (black on white) to a one-colour, self-typing ASCII SVG."""
import numpy as np
from PIL import Image
COLS, RAMP = 90, " .`:-=+*cs#%@"
im = Image.open("emblem-source.png").convert("L")
a = np.array(im); ys, xs = np.where(a < 200)
im = im.crop((xs.min() - 20, ys.min() - 20, xs.max() + 20, ys.max() + 20))
rows = max(1, int(COLS * im.height / im.width * 0.5))
g = np.array(im.resize((COLS, rows), Image.LANCZOS)) / 255.0
lines = ["".join(RAMP[min(len(RAMP) - 1, int((1 - v) ** 0.8 * len(RAMP)))] for v in r).rstrip() for r in g]
CW, LH = 7.2, 13; W, H = int(COLS * CW) + 20, rows * LH + 30
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,Menlo,monospace" font-size="12">',
     f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/>', "<defs>"]
for i in range(len(lines)):
    o.append(f'<clipPath id="c{i}"><rect x="10" y="{16+i*LH}" width="0" height="{LH}"><animate attributeName="width" from="0" to="{W}" dur="0.5s" begin="{i*0.07:.2f}s" fill="freeze"/></rect></clipPath>')
o.append("</defs>")
for i, l in enumerate(lines):
    o.append(f'<text clip-path="url(#c{i})" x="10" y="{16+(i+1)*LH-3}" fill="#c9d1d9" xml:space="preserve">{l.replace("&","&amp;").replace("<","&lt;")}</text>')
o.append("</svg>"); open("avi-ascii.svg", "w").write("\n".join(o)); print(W, H, rows)
print("\n".join(lines))
