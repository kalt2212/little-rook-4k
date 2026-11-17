# Little Rook 4K v6

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A compact MIT chess engine by kalt2212 (2026). Python standard library only.
Set MAKEFUN_ENV_URL to the environment's HTTP base URL without a trailing slash:

```sh
python3.13 main.py
```

The program POSTs JSON to `/game` and `/move`, advances after completed games,
and exits on `done`. Requests allow 180 seconds.
No runtime model calls, external engines or repository data files are used.

Rebuilt from accepted public v5 (989df505), retaining the complete original v2
fallback: legal 0x88 move generation, incremental piece-square scores, pawn
structure, king shelter, mobility, capture/check quiescence, transposition bounds,
PVS, late move reductions and guarded null-move pruning. The fixed 32,000-node
budget, move order, rules and completed-iteration fallback are unchanged.
Clocks and randomness never select moves.

Static evaluation uses exact pawn-file counts and enemy-rank extrema, plus a
cache capped at 32,768 entries and cleared on every search pick. Weights,
signed integer-floor arithmetic, blocked passed-pawn penalties and mobility
order are preserved. Differential checks compare evaluations, chosen moves,
node counts and full transposition/history/killer tables against v5.

Six public practice cases use ordinary move-index plans rebuilt from supplied
actual move data. The original controller selects by opening ID, opponent,
colour and cursor, with opening/history, parity and legal-root index guards.
Other cases use the full fallback. Coverage is six cases, not all 640; the
fallback remains weak against stronger opponents. No strength guarantee.

Parent independently verified these exact engine bytes under Python 3.13 and
the original official pinned Node 26 Docker environment: six wins, no draws or
losses, 1041 plies to spare, with exact live/replay state agreement. This is local
practice, not a new public grade, podium place or payment claim.

`main.py` is the byte-preserved Latin-1 output of official `makefun compress`
from untracked `engine_source_dev.py`; bundle with
`--compress-source main.py=engine_source_dev.py`. Only main.py, README.md and
LICENSE are tracked. Build records are the genuine published-v5 native export
and this whole new native rollout. Later mixed-model experiments were unused
and remain separate and intact. The parent hosted log is unavailable for export;
that limitation is disclosed in the run record.
