"""Builds the site's pages from one shared shell (nav + footer). Run: python3 tools/build.py

Page bodies live in src/*.html; scam cards come from scams.json at view time.
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINKS = [("YouTube", "https://www.youtube.com/@scamray", "youtube"),
         ("Instagram", "https://www.instagram.com/thescamray", "instagram"),
         ("TikTok", "https://www.tiktok.com/@thescamray", "tiktok")]
ICONS = {'youtube': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1c.4-1.6.5-3.2.5-4.8s-.1-3.2-.5-4.8zM9.7 15.1V8.9l5.8 3.1-5.8 3.1z"/></svg>', 'instagram': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zm0 4.6a5.2 5.2 0 1 0 0 10.4 5.2 5.2 0 0 0 0-10.4zm0 8.6a3.4 3.4 0 1 1 0-6.8 3.4 3.4 0 0 1 0 6.8zm5.4-9.9a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4z"/></svg>', 'tiktok': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.6 2h-3.4v13.4a2.9 2.9 0 1 1-2.9-2.9c.3 0 .6 0 .9.1V9.2a6.3 6.3 0 1 0 5.4 6.2V8.6a8 8 0 0 0 4.7 1.5V6.7a4.7 4.7 0 0 1-4.7-4.7z"/></svg>'}

PAGES = {
    "index": ("Scam Ray: scams explained in under a minute", "Scam Ray takes one real scam apart in under a minute: what it looks like, the red flag, and what to do instead."),
    "scams": ("All scams | Scam Ray", "Every scam Scam Ray has broken down, sortable and filterable."),
    "about": ("About | Scam Ray", "Who makes Scam Ray and why."),
    "privacy": ("Privacy Policy | Scam Ray", "Scam Ray's Privacy Policy."),
    "terms": ("Terms of Service | Scam Ray", "Scam Ray's Terms of Service."),
}


def ver(path):
    """Content hash for cache busting, so visitors get new CSS/JS as soon as a deploy lands."""
    return hashlib.sha1((ROOT / path).read_bytes()).hexdigest()[:8]


def shell(name, body):
    title, desc = PAGES[name]
    menu = "".join(f'<a href="{u}">{ICONS[i]}{n}</a>' for n, u, i in LINKS)
    social = "".join(f'<a href="{u}" aria-label="{n}">{ICONS[i]}</a>' for n, u, i in LINKS)
    cur = lambda p: ' aria-current="page"' if p == name else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="assets/favicon-v3.png" sizes="48x48"><link rel="icon" href="assets/favicon-v3.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="assets/apple-touch-icon-v3.png"><link rel="stylesheet" href="style.css?v={ver('style.css')}"><script src="assets/site.js?v={ver('assets/site.js')}" defer></script></head>
<body>
<header class="site-head"><div class="wrap"><nav class="nav"><a class="logo" href="index.html">SCAM <span>RAY</span></a>
<div class="links"><a href="scams.html"{cur("scams")}>Scams</a><a href="about.html"{cur("about")}>About</a>
<details class="watch"><summary>Watch on</summary><div class="menu">{menu}</div></details></div></nav></div></header>
{body}
<div class="wrap"><footer><div class="social">{social}</div>
<div class="flinks"><span>© 2026 Scam Ray</span><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a><a href="mailto:scamray@googlegroups.com">Contact</a></div></footer></div>
</body></html>
"""


for name in PAGES:
    body = (ROOT / "src" / f"{name}.html").read_text()
    if name in ("privacy", "terms"):
        body = f'<main class="wrap"><div class="doc">\n{body}</div></main>'
    (ROOT / f"{name}.html").write_text(shell(name, body))
print("built", ", ".join(PAGES))
