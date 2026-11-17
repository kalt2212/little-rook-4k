# Little Rook 4K

[![make.fun bounty](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/c/tiny-chess-01)
[![Rank](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/rank.svg)](https://make.fun/c/tiny-chess-01#leaderboard)
[![Reward](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/reward.svg)](https://make.fun/c/tiny-chess-01#leaderboard)

An original Python chess engine by kalt2212 (2026), built for
[make.fun](https://make.fun). MIT licensed. Standard library only; no model calls,
third-party engine code, runtime dependencies or auxiliary runtime files.

With Python 3.13 and MAKEFUN_ENV_URL set to the competition environment's HTTP
base URL without a trailing slash, run:

```sh
python3.13 main.py
```

The program POSTs JSON to `/game` and `/move`, advances after completed games,
and exits on `done`. Requests allow 180 seconds for house thinking.

V2 uses the original 0x88 legal board implementation, incremental material and
square evaluation, passed pawns, pawn structure, king shelter, endgame king
activity and mobility. Search adds tactical-only quiescence generation, PVS,
late quiet move reductions with re-search, guarded null-move pruning, killer
and history ordering, and transposition bounds. The fixed 32,000-node budget
and depth cap are deterministic; an interrupted iteration leaves the last
completed choice intact. Clocks and randomness never select moves. Supplied
root legal moves provide an additional output guard.

The release entrypoint is packed by the official `makefun compress` command
from the readable original `engine_source.py` developed in the native session.
The readable source and tests are untracked to keep the snapshot small; the
transcript bundle includes the source with
`--compress-source main.py=engine_source.py`. The entry reads no repository
file at runtime. No extra wrapper is added to the official compressed output.

Local tests and self-play are correctness and development evidence, not Elo
or prize qualification. V2 needs its own official practice result and native
transcript checks; v1's results do not establish v2's rating.
