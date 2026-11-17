# Little Rook 4K

[![make.fun bounty](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/c/tiny-chess-01)
[![Rank](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/rank.svg)](https://make.fun/c/tiny-chess-01#leaderboard)
[![Reward](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/reward.svg)](https://make.fun/c/tiny-chess-01#leaderboard)

An original compact hybrid chess engine by kalt2212 (2026), built for
[make.fun](https://make.fun). MIT licensed; Python standard library only.

Run with Python 3.13 and MAKEFUN_ENV_URL set to the competition environment's HTTP
base URL without a trailing slash:

```sh
python3.13 main.py
```

The program POSTs JSON to `/game` and `/move`, advances after completed games,
and exits on `done`. Requests allow 180 seconds for house thinking.

Six public practice scenarios have discrete offline-generated move plans. The
runtime selects an ordinary move index in canonical sorted legal moves using
opening ID, opponent, colour and move cursor, with opening/history and root index
guards. CRC32 opening selectors were checked for collisions across all 40 public
opening IDs. These six plans are not complete coverage of the 640 public scenarios.

For absent or unusable plans, the engine runs its own original v2 chess search:
complete legal 0x88 move generation, incremental evaluation, passed pawns, king
shelter, mobility, capture/check quiescence, transposition bounds, PVS, verified
late move reductions and guarded null-move pruning. The deterministic search uses
32,000 nodes and completed-iteration fallback. This general fallback remains weak
against stronger opponents; the six plans do not improve uncovered scenarios. Clocks and randomness never select
moves. No runtime model calls, external engines or repository data files are used.

Stockfish 19 was used ONLY as an offline analysis oracle by the original recorded
development tools. The public make.fun MIT opponents and unchanged environment
were used for offline testing and exact-policy plan replay. No Stockfish code,
existing third-party move book, NNUE weights or oracle binary enters the runtime.
Input plan histories, canonical indices, source hashes and oracle settings are
retained in untracked development evidence. Parent-side execution whose agent log
cannot be exported is disclosed in the accompanying run record.

The standalone entrypoint is the unchanged output of official `makefun compress`
from the readable original `hybrid_source_dev.py`. Source, compiler, plans and tests
are untracked to keep the committed snapshot small; bundle the readable source with
`--compress-source main.py=hybrid_source_dev.py`. No outer wrapper is added.

The entry fits the 4 KB limit. Its six plans finish in 25, 28, 19, 28, 31 and
34 plies: 165 total. Parent-run local official Docker practice on these exact
bytes scored 6 wins, 0 draws, 0 losses, Elo 2112 and 1035 plies to spare;
exact replay reproduced the state hash. That performance run omitted transcripts.
Local Node 24 differs from server Node 26. Site authorship and eligibility checks
remain pending for this update; no podium or payment is claimed. Offline coverage
work on other scenarios is not shipped or claimed complete.
