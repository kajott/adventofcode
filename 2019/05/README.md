# 2019, Day 5: Sunny with a Chance of Asteroids


## Solution Notes

Intcode slowly evolves to a properly usable ISA; whith the comparison and `jz`/`jnz` instructions, it doesn't even rely on self-modifying code to do anything meaningful any longer. The interpreter starts to become unwieldy though, especially in the golf version.

As for the puzzle itself, it's just straightforward emulation, with no surprises whatsoever.

* Part 1, Python: 271 bytes, <100 ms
* Part 2, Python: 342 bytes, <100 ms
