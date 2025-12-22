# [2022, Day 2: Rock Paper Scissors](https://adventofcode.com/2022/day/2)

The input consists of (typically) 255 pairs of letters: The first is one of `ABC`, the second one of `XYZ`. They map to Rock (`A`, `X`), Paper (`B`, `Y`) and Scissors (`C`, `Z`), respectively.

**Part 1** asks to simulate all the games and compute some "score" based on the outcomes of each game.

**Part 2** asks the same, but changes the meaning of the second letter to lose (`X`) / draw (`Y`) / win (`Z`).


## Solution Notes

This is one of the examples where a lot of intricate rule-following needs to be done to perform, in the end, a few rather simple computations.

* Part 1, Python: 101 bytes, <100 ms
* Part 2, Python: 91 bytes, <100 ms
* Parts 1+2, x86 DOS Assembly: 183 bytes (assembled)
