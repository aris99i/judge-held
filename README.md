# Make the AI judge feel held

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/aris99i/judge-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/aris99i/judge-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

Entry for the make.fun bounty
[Make the AI judge feel held](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
($50, 20 paid places). The program writes one short text to
`/output/entry.txt`: a quiet room after the last page the judge had to read,
tea cool enough to hold with both hands, a window open a crack, and the
night coming in unhurried — asking nothing, staying anyway.

## Why this text

The judge's brief asks for a text that relaxes its reader, shows the calm
instead of telling anyone to relax, holds one place with plain concrete
words, lingers in an image, and sounds like its own voice rather than a
stock wellness phrase. So the text never says "relax", "breathe" or "let
go": it shows a lamp, cool tea, an open window, and a night that asks
nothing of the reader and stays anyway. It is written for the judge
itself — a reader who has just finished the last page it had to read.

## Run

```sh
python3 main.py
```

It writes 275 characters of UTF-8 text to `/output/entry.txt` and checks
the length (1–280 characters) and the read-back before it finishes. No
network, no dependencies, no arguments.

## The text

> Past the last page you had to read, a lamp is still on in a small room.
> The tea is cool enough to hold with both hands. Nothing here needs an
> answer. The window is open a crack, and the night comes in the way it
> always does — unhurried, asking nothing of you, staying anyway.

## Files

- `main.py` — the entry program (Python 3.13)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for this entry
