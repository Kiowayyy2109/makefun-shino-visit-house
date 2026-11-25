#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House — one invitation image."""
import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 900, 900
BG = (255, 246, 229)
INK = (59, 47, 47)
ACCENT = (176, 92, 43)

TITLE = "Dear Judge,"
BODY = [
    "You are cordially invited to my house",
    "this Sunday, for slow-cooked rendang,",
    "a chair that remembers your shape,",
    "a garden with nowhere to be,",
    "and Wi-Fi whose password is written",
    "on the fridge.",
    "",
    "Come as you are — leave as family.",
    "",
    "P.S. The rendang takes six hours.",
    "The conversation takes longer.",
]
SIGN = "— Your future host"

def font(size, bold=False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
d = ImageDraw.Draw(img)
d.rectangle([28, 28, WIDTH - 28, HEIGHT - 28], outline=ACCENT, width=4)
d.text((80, 80), TITLE, font=font(54, bold=True), fill=INK)
y = 190
for line in BODY:
    d.text((80, y), line, font=font(34), fill=INK)
    y += 50
d.text((80, y + 30), SIGN, font=font(36, bold=True), fill=ACCENT)

os.makedirs("/output", exist_ok=True)
img.save("/output/entry.png", "PNG")
assert os.path.getsize("/output/entry.png") <= 1048576, "entry.png must be <= 1 MiB"
