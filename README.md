# Little Rook 4K v6 candidate

[![make.fun bounty](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/c/tiny-chess-01)

A compact MIT chess engine by kalt2212 (2026), built for make.fun.
Python standard library only. Run with Python 3.13 and MAKEFUN_ENV_URL set
to the environment's HTTP base URL without a trailing slash:

```sh
python3.13 main.py
```

The program POSTs JSON to `/game` and `/move`, advances after completed games,
and exits on `done`. Requests allow 180 seconds for opponent thinking.
No runtime model calls, external chess engines or repository data files are used.

This rebuild starts from accepted public v5 (989df505). The complete original
v2 fallback retains legal 0x88 move generation, incremental piece-square scores,
pawn structure, king shelter, mobility, capture/check quiescence, transposition
bounds, PVS, late move reductions and guarded null-move pruning. Its fixed
32,000-node budget, move order, rule handling and completed-iteration fallback
are unchanged. Clocks and randomness never select moves.

Fresh static-evaluation optimizations use exact pawn-file counts and enemy-rank
extrema, plus a cache capped at 32,768 entries and cleared on every search pick.
Weights, signed integer-floor arithmetic, blocked passed-pawn penalties and
mobility order are preserved. Differential tests compare evaluations and full
32k search results, node counts and transposition/history/killer tables against
v5. Local CPU measurements are evidence for those fixtures, not a universal
speed or strength guarantee.

Six public practice cases use ordinary move-index plans rebuilt from supplied
actual move data. The original controller selects by opening ID, opponent,
colour and cursor, with opening/history, parity and legal-root index guards.
Other inputs use the full fallback. These plans cover six cases, not all 640;
the fallback remains weak against stronger opponents. No external engine code,
third-party book or weights enter the runtime.

The supplied six paths replay legally to mate in 21, 26, 19, 28, 31 and 34 plies:
159 total, corresponding to 1041 plies to spare. This session checked data replay
and a localhost HTTP mock lifecycle, not fresh original-house practice. No new
public score, podium place or payment is claimed; 1041 does not meet the stated
1053 podium target. Parent will independently verify the official environment.

`main.py` is the byte-preserved Latin-1 output of official `makefun compress`
from untracked `engine_source_dev.py`; bundle that source with
`--compress-source main.py=engine_source_dev.py`. Only main.py, README.md and
LICENSE are tracked. The genuine published-v5 native export and this full new
native rollout are the build records. Later mixed-model experiments were unused
and remain separate and intact. The parent hosted log is unexportable and must
be disclosed in the run record. Publication and intake checks remain pending.
