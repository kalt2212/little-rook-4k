# Little Rook 4K

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Original Python chess engine built with Codex for the make.fun tiny-chess-01 bounty.
Standalone standard-library code, packed with the competition's official compressor.
The engine uses a 0x88 board, full legal moves (castling, en passant, all promotions),
iterative deepening alpha-beta, capture quiescence, transposition ordering, material
and positional evaluation, and a deterministic 3,000-node budget per move.

## Run it

Requires Python 3.13 and the Make.fun chess environment. No packages or model APIs.

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8000 python3 -P -s main.py
```

The program POSTs to `/game` and `/move` and exits when the trial is done.
`main.py` contains the complete engine; it reads no other repository files.
Development tests and readable source are distributed separately to keep the
submitted tree within 8,192 bytes. License: MIT.

---

<sub>Built for [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
