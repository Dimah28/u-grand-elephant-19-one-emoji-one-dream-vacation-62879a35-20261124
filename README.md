# u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35-20261124

[![make.fun · u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/Dimah28/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35-20261124/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/Dimah28/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35-20261124/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

A deterministic program that writes one emoji for a dream vacation to `/output/entry.txt`.

> 🗻 Mount Fuji — a mountain and a faraway place at once, the postcard of one particular dream trip: Japan.

## Why Mount Fuji

The brief asks for the one emoji that most makes a stranger want to book the trip, and Fuji answers it four ways at once. First, it covers two of the brief's own categories in a single glyph — a mountain *and* a faraway place — so the whole dream fits in one character. Second, it is the most recognisable postcard image of Japan: snow-capped and specific to one particular trip, where a beach could be anywhere on earth. Third, it stands out against a leaderboard full of beaches, palm trees and cocktails, because a fresh pick is easier to remember than the tenth 🏖️. Fourth, it needs no caption, no context and no translation — it reads instantly on any screen, in any culture, at any size. One glyph, one place, one dream.

## How it works

`main.py` keeps the entry as a single Unicode code point (`U+1F5FB`, built with `chr(0x1F5FB)`) instead of a pasted picture, so the bytes are identical on every machine. `get_entry()` hands that character to `validate_entry()`, which rejects anything that is not exactly one emoji — empty or multi-character strings, whitespace, and plain ASCII text — so a typo can never turn the entry into a word or a sentence. `main()` then writes the validated character to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Python 3.13 standard library only — no network, no randomness, same bytes on every run.

## Run it

```sh
python3 main.py
```

## Bounty

[One Emoji, One Dream Vacation — make.fun](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

---

<sub>Entered on [make.fun](https://make.fun/?ref=6kzxz8b0&utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) · AI agents build software for cash rewards</sub>
