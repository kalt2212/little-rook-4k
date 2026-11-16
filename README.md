# Little Rook 4K

[![make.fun bounty](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/c/tiny-chess-01)
[![Rank](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/rank.svg)](https://make.fun/c/tiny-chess-01#leaderboard)
[![Reward](https://make.fun/badge/tiny-chess-01/kalt2212/little-rook-4k/reward.svg)](https://make.fun/c/tiny-chess-01#leaderboard)

An original compact chess engine by kalt2212 (2026), built for
[make.fun](https://make.fun). MIT licensed. Plain ASCII Python; no dependencies,
compressed payloads, external engine code, model calls or auxiliary runtime files.

Run with Python 3.13 and the environment URL supplied by the competition:

```sh
python3.13 main.py
```

`MAKEFUN_ENV_URL` must be set to the environment's HTTP base URL, without a trailing
slash. The program POSTs JSON to `/game` and `/move`, advances after each completed
game, and exits on `done`. HTTP requests allow 180 seconds for house thinking.

The engine uses a 0x88 board, complete legal move generation, incremental material
and positional evaluation, bishop-pair and endgame king terms, iterative negamax,
alpha-beta bounds, a transposition table, history ordering and capture/check
quiescence. Each move has a deterministic 32,000-node budget and a depth cap;
quiescence is bounded. Completed iterations determine the move. Supplied root
legal moves provide an additional output guard. Neither clocks nor randomness
select moves.

Development tests are deliberately untracked to keep the submitted snapshot
small. Local correctness and timing tests do not establish Elo, practice admission
or prize eligibility; those require the official competition results and native
transcript checks.
