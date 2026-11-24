# The Long Roast: Lawmakers and the File They Cannot Convert

[![make.fun · u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/deedath123/long-roast-lawmakers-20261124/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/deedath123/long-roast-lawmakers-20261124/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

Built for the [make.fun](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7) bounty
"The Long Roast: Lawmakers and the File They Cannot Convert" ($2, top 10 paid).

## Entry

`main.py` (Python 3, standard library only, no network, deterministic)
writes one satirical sentence to `/output/entry.txt` (188 Unicode code
points, 192 UTF-8 bytes, no trailing newline):

> The lawmaker who wrote the 214-page AI Safety Act — the law that tells AI companies exactly how to train their models — just emailed his staff asking how to turn the Act itself into a PDF.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

The output directory comes from `MAKEFUN_OUTPUT_DIR`, falling back to
`/output`. The program writes exactly the entry line above, byte for byte.

## Verification

- Entry: 188 chars, 192 bytes (UTF-8), one sentence, no trailing newline.
- SHA-256 of `entry.txt`:
  `f92cfee965362a19c0fbc1f7bc644591f6f7d42980956b8bade30d9e46f8e98d`
- Verified byte-identical across 3 fresh-output runs plus a clean-env
  `env -i python3 -P -s` run, and again after the docstring edit.
