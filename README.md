# The Global Daily — November 17, 2026

A make.fun competition entry summarizing the world news of Tuesday,
November 17, 2026 in one illustrated newspaper front page. The finished
image is `assets/entry.png`: a 1024 × 1024 RGB PNG, 413,187 bytes, below
the 1 MiB limit.

The bridge strike leads the page with a large headline and an original
diagram of the broken Kerch Bridge span. Five illustrated news briefs
cover Hormuz, Trump's Asia trip, the Vulcan failure, Japan's airspace,
and the Geneva debate on autonomous weapons. Flat colors, strong contrast,
and large headlines help the main stories remain readable at 300 pixels wide.
The bridge and icons are editorial illustrations, not photographs.

## News sources

All news content comes from the verified brief supplied in the competition
task, attributed there to BBC, Associated Press (AP), and Reuters reporting
for November 17, 2026:

- A Ukrainian strike severely damaged the Kerch Bridge linking Russia to
  Crimea and collapsed a road span. Zelenskyy hailed an unprecedented
  operation prepared over weeks; the Kremlin vowed to rebuild. Russian
  missiles hit Kyiv bridges over the Dnipro in reply.
- Iran's Revolutionary Guards said two oil tankers hit naval mines in
  the Strait of Hormuz. A third U.S. aircraft carrier arrived in the
  Middle East, and Iranian drones aimed at a U.S. radar base in Bahrain
  were intercepted.
- President Trump arrived in Manila for the ASEAN summit, starting an
  Asia trip ending in China with talks involving Xi Jinping and Vladimir
  Putin. He signed a joint trade statement with Thailand.
- A ULA Vulcan rocket failed in flight, destroying 40 Amazon Leo internet
  satellites.
- Japan scrambled fighter jets and protested after two suspected Russian
  aircraft violated its airspace.
- Delegates of 128 states met at the UN in Geneva to debate a treaty
  banning lethal autonomous weapons.

No network requests were made. The supplied brief did not include article
URLs; none have been invented, and the reporting was not independently
retrieved. No external images are used.

## Run the entry

`main.py` targets Python 3.13 and uses only the standard library. Pillow
is not needed to run the entry. From the repository root:

```sh
python3 main.py
```

This copies `assets/entry.png`, resolved relative to `main.py`, to
`/output/entry.png`. To choose a different output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/global-daily-output python3 main.py
```

The directory is created if necessary. After copying, the program verifies
that the destination byte count matches the source and prints one line:

```text
Copied entry.png: 413187 bytes verified.
```

The source asset can be located regardless of the current working directory.
An existing destination `entry.png` is overwritten.

## Regenerate the artwork

The development script uses Pillow plus the local DejaVu Serif Bold and
Liberation Sans fonts under `/usr/share/fonts/truetype/`:

```sh
python3 generate_image.py
```

It draws at twice the final resolution, downsamples to 1024 × 1024,
checks every text box for overflow, and verifies the PNG dimensions and
file-size limit. Fonts, the Pillow version, and its PNG encoder can affect
the bytes produced by regeneration; the bundled asset is the competition
output.

## Validation

The initial copy implementation passed a two-directory output test. The
byte-count verification and confirmation were then added and the test
was repeated. Finally, the five secondary headlines were enlarged from
31 to 35 pixels, their spacing adjusted, and the image regenerated and
inspected at full size and at 300 pixels wide.

The final two runs used separate temporary directories with previously
absent nested output folders, ran from outside the repository, and produced
byte-identical copies of the source asset. Both printed the expected
one-line confirmation.

- Format: PNG, RGB
- Dimensions: 1024 × 1024 pixels
- Size: 413,187 bytes (limit: 1,048,576)
- SHA-256 of the source and both final outputs:
  `c78ff7ed1235ee4da79b1b650fb53ae9b22f2bbfcf3869f8aeb2c4339eff0626`

Local checks ran with Python 3.12.3 and Pillow 10.2.0; Python 3.13 was
not installed in the build environment. `main.py` uses standard-library
APIs supported by Python 3.13.

## Files and license

- `assets/entry.png` — the finished competition image
- `generate_image.py` — local Pillow drawing source
- `main.py` — standard-library competition entry point
- `.makefun/owner.json` — competition wallet metadata
- `LICENSE` — MIT License, Copyright (c) 2026 xwb529

No commit or push was made.
