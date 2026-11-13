# -*- coding: utf-8 -*-
import glob
import html
import re

bad = re.compile(r",\s*,|,,|\.,|,\.|,\s{2,}|\(, |: ,|\s,")
tot = 0
for f in sorted(glob.glob("dist/**/index.html", recursive=True)):
    f2 = f.replace(chr(92), "/")
    if "/kit/" in f2:
        continue
    s = open(f, encoding="utf-8").read()
    body = s[s.index("<main"):s.index("</main>")]
    t = html.unescape(re.sub(r"<[^>]+>", " ", body))
    for m in bad.finditer(t):
        tot += 1
        print(f2[5:35], "...", t[max(0, m.start() - 50):m.end() + 40].replace("\n", " "))
print(tot)
