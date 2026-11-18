#!/usr/bin/env python3
"""Draw the competition image with Pillow; no external images or network access."""

from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "assets" / "entry.png"
WIDTH = HEIGHT = 1024
SCALE = 2
PAPER = "#F7F3E9"
INK = "#152A34"
RED = "#A82D26"
TEAL = "#185D6D"
PALE = "#DBE8E7"
RULE = "#9AA5A1"
FONT_ROOT = Path("/usr/share/fonts/truetype")
FONT_FILES = {
    "masthead": FONT_ROOT / "dejavu/DejaVuSerif-Bold.ttf",
    "bold": FONT_ROOT / "liberation/LiberationSans-Bold.ttf",
    "regular": FONT_ROOT / "liberation/LiberationSans-Regular.ttf",
}

image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), PAPER)
draw = ImageDraw.Draw(image)
text_boxes = []


def font(size, face="regular"):
    return ImageFont.truetype(str(FONT_FILES[face]), round(size * SCALE))


def box(bounds, fill, outline=None, width=1):
    draw.rectangle(tuple(round(v * SCALE) for v in bounds), fill=fill,
                   outline=outline, width=round(width * SCALE))


def line(points, fill=INK, width=1):
    draw.line([(round(x * SCALE), round(y * SCALE)) for x, y in points],
              fill=fill, width=round(width * SCALE), joint="curve")


def polygon(points, fill, outline=None, width=1):
    points = [(round(x * SCALE), round(y * SCALE)) for x, y in points]
    draw.polygon(points, fill=fill)
    if outline:
        draw.line(points + [points[0]], fill=outline,
                  width=round(width * SCALE), joint="curve")


def ellipse(bounds, fill, outline=None, width=1):
    draw.ellipse(tuple(round(v * SCALE) for v in bounds), fill=fill,
                 outline=outline, width=round(width * SCALE))


def text(value, x, y, size, face="regular", fill=INK, right=992, bottom=1024):
    """Place text by its visible upper left, and fail on any overflow."""
    f = font(size, face)
    bounds = draw.textbbox((x * SCALE, y * SCALE), value, font=f, anchor="lt")
    bounds = tuple(v / SCALE for v in bounds)
    assert bounds[0] >= 0 and bounds[1] >= 0, (value, bounds)
    assert bounds[2] <= right and bounds[3] <= bottom, (value, bounds, right, bottom)
    text_boxes.append((value, bounds))
    draw.text((round(x * SCALE), round(y * SCALE)), value,
              font=f, fill=fill, anchor="lt")


def star(cx, cy, radius, fill=INK):
    points = []
    for i in range(16):
        angle = math.pi * i / 8
        r = radius if i % 2 == 0 else radius * 0.43
        points.append((cx + math.cos(angle) * r, cy + math.sin(angle) * r))
    polygon(points, fill)


def tanker(x, y):
    polygon([(x+5,y+32),(x+83,y+32),(x+73,y+49),(x+19,y+49)], INK)
    box((x+15,y+18,x+31,y+31), INK)
    box((x+18,y+12,x+25,y+18), INK)
    box((x+19,y+21,x+26,y+25), PAPER)
    for dx in (38, 53, 68):
        box((x+dx,y+25,x+dx+10,y+31), TEAL)
    line([(x+9,y+55),(x+25,y+57),(x+42,y+55),(x+59,y+57)], TEAL, 2)
    star(x+80, y+60, 8, RED)


def airplane(x, y):
    polygon([(x+45,y+5),(x+49,y+12),(x+49,y+29),(x+84,y+46),
             (x+84,y+52),(x+49,y+44),(x+49,y+59),(x+59,y+66),
             (x+59,y+70),(x+45,y+66),(x+31,y+70),(x+31,y+66),
             (x+41,y+59),(x+41,y+44),(x+6,y+52),(x+6,y+46),
             (x+41,y+29),(x+41,y+12)], TEAL)


def rocket(x, y):
    line([(x+13,y+57),(x+25,y+45)], TEAL, 2)
    line([(x+9,y+44),(x+23,y+35)], TEAL, 2)
    polygon([(x+28,y+43),(x+35,y+22),(x+65,y+6),(x+72,y+6),
             (x+72,y+13),(x+57,y+43),(x+36,y+50)], INK)
    polygon([(x+28,y+43),(x+16,y+40),(x+36,y+27)], RED)
    polygon([(x+36,y+50),(x+39,y+63),(x+55,y+44)], RED)
    ellipse((x+49,y+18,x+61,y+30), PALE)
    star(x+26, y+57, 11, RED)
    for dx, dy in ((68, 50), (79, 36), (58, 65)):
        box((x+dx,y+dy,x+dx+5,y+dy+5), TEAL)


def fighter(x, y):
    polygon([(x+45,y+5),(x+50,y+26),(x+82,y+51),(x+81,y+58),
             (x+53,y+48),(x+54,y+60),(x+64,y+67),(x+62,y+72),
             (x+45,y+66),(x+28,y+72),(x+26,y+67),(x+36,y+60),
             (x+37,y+48),(x+9,y+58),(x+8,y+51),(x+40,y+26)], INK)
    line([(x+45,y+29),(x+45,y+46)], PAPER, 3)
    ellipse((x+72,y+8,x+83,y+19), RED)


def robot(x, y):
    line([(x+45,y+10),(x+45,y+21)], INK, 3)
    ellipse((x+41,y+3,x+49,y+11), RED)
    box((x+18,y+21,x+72,y+61), INK)
    box((x+10,y+32,x+18,y+49), TEAL)
    box((x+72,y+32,x+80,y+49), TEAL)
    box((x+28,y+31,x+38,y+41), PAPER)
    box((x+52,y+31,x+62,y+41), PAPER)
    line([(x+32,y+51),(x+58,y+51)], PAPER, 3)
    line([(x+29,y+65),(x+61,y+65)], TEAL, 3)


def bridge():
    """An editorial diagram: a road span broken and tipped into the sea."""
    box((32, 294, 992, 444), PALE)
    polygon([(32,389),(123,381),(238,386),(359,381),(459,390),
             (602,385),(714,390),(844,381),(992,387),(992,411),(32,411)],
            "#AFCCCB")
    box((32, 402, 992, 444), TEAL)
    for px in (92, 222, 352, 482, 764, 894):
        polygon([(px-8,361),(px+8,361),(px+12,418),(px-12,418)], "#8EABA9")
    # Smoke rises at the broken joint; muted flat shapes preserve contrast.
    for bounds in ((530,329,560,367), (519,315,552,349),
                   (540,308,570,337), (554,299,581,324)):
        ellipse(bounds, "#9AA5A1")
    polygon([(32,350),(528,350),(536,356),(525,363),(32,363)], INK)
    polygon([(711,350),(992,350),(992,363),(703,363),(711,358)], INK)
    line([(32,346),(525,346)], "#668B91", 3)
    line([(715,346),(992,346)], "#668B91", 3)
    for px in list(range(50, 525, 25)) + list(range(725, 990, 25)):
        line([(px,345),(px,351)], INK, 2)
    # One deck segment falls diagonally into the water, separated at both ends.
    polygon([(549,359),(559,350),(677,419),(668,432)], INK)
    line([(559,353),(676,421)], "#8EABA9", 3)
    for px, py in ((660,433),(692,432),(727,423)):
        line([(px-9,py),(px,py-4),(px+9,py)], "#D3E5E0", 2)
    for px, py in ((66,429),(179,416),(316,433),(437,421),(840,431),(938,419)):
        line([(px,py),(px+39,py)], "#6A9B9F", 2)
    text("KERCH BRIDGE", 47, 306, 18, "bold", bottom=331)
    text("RUSSIA–CRIMEA LINK", 786, 307, 16, "bold", right=978, bottom=331)


def story(y, headline, summary, icon, headline_size=35):
    line([(32, y), (992, y)], RULE, 1)
    icon(41, y + 7)
    text(headline, 146, y + 7, headline_size, "bold", bottom=y + 38)
    for i, sentence in enumerate(summary):
        text(sentence, 146, y + 39 + i * 23, 23, bottom=y + 84)


def main():
    text("THE GLOBAL DAILY", 32, 21, 78, "masthead", bottom=91)
    line([(32, 98), (992, 98)], INK, 4)
    text("TUESDAY, NOVEMBER 17, 2026", 32, 111, 34, "bold", bottom=145)
    line([(32, 151), (992, 151)], INK, 1)
    text("UKRAINE STRIKE COLLAPSES", 32, 166, 61, "bold", RED, bottom=217)
    text("CRIMEA BRIDGE SPAN", 32, 228, 68, "bold", INK, bottom=284)
    bridge()
    text("Zelenskyy hails an unprecedented operation, weeks in the making.",
         32, 456, 25, bottom=480)
    text("Kremlin vows to rebuild. In reply, Russian missiles hit Kyiv’s",
         32, 485, 25, bottom=509)
    text("bridges over the Dnipro River.", 32, 514, 25, bottom=538)

    story(550, "HORMUZ: TWO TANKERS HIT MINES", [
        "Iran’s Guards report mine hits; 3rd U.S. carrier in region.",
        "Iranian drones aimed at U.S. radar base in Bahrain intercepted.",
    ], tanker)
    story(637, "TRUMP IN MANILA FOR ASEAN", [
        "Asia trip ends in China for talks involving Xi and Putin.",
        "Joint trade statement signed with Thailand.",
    ], airplane)
    story(724, "VULCAN FAILS: 40 AMAZON SATELLITES LOST", [
        "ULA rocket fails in flight, destroying 40 Amazon Leo",
        "internet satellites.",
    ], rocket)
    story(811, "JAPAN SCRAMBLES JETS, PROTESTS", [
        "Two suspected Russian aircraft violate Japanese airspace;",
        "Tokyo responds with fighters and a protest.",
    ], fighter)
    story(898, "128 STATES DEBATE AUTONOMOUS ARMS BAN", [
        "UN delegates in Geneva debate a treaty banning",
        "lethal autonomous weapons.",
    ], robot)

    line([(32, 988), (992, 988)], INK, 2)
    text("NEWS BRIEF: BBC / AP / REUTERS", 32, 998, 15, "bold", bottom=1016)
    text("ILLUSTRATED DAILY SUMMARY", 755, 998, 15, "bold", bottom=1016)
    final = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    final.save(OUTPUT, format="PNG", optimize=True)
    size = OUTPUT.stat().st_size
    assert size <= 1048576, f"PNG exceeds 1 MiB: {size} bytes"
    with Image.open(OUTPUT) as check:
        assert check.format == "PNG" and check.size == (1024, 1024)
    print(f"Drew {len(text_boxes)} checked text boxes: {OUTPUT.name}, "
          f"{WIDTH}x{HEIGHT}, {size} bytes")


if __name__ == "__main__":
    main()
