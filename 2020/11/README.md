# [2020, Day 11: Seating System](https://adventofcode.com/2020/day/11)


## Solution Notes

A straightforward 2D cellular automaton simulation, albeit with three possible states.

I tried two different implementations for part 1 here: first the "classical" way with a two-dimensional array, and then using the good old "dictionary indexed by complex number" trick. The latter is slower, but considerably smaller, and it forms a formidable base for part 2: The only difference is that except looking for the immediate neighbors, there's a little scan routine that increments the position by the delta until a seat is found. Border handling is quite costly though, but that would be the case either way.

Out of curiosity, I also implemented a (non-golf) C version to see just how fast it is, and sure enough, it's 20x as fast as the Python version, **including** compilation: ~150 ms. (Without compilation, it's 100x.)

* Part 1, Python (with 2D arrays): 347 bytes, ~1.5 s
* Part 1, Python (with dictionaries): 269 bytes, ~2.5 s
* Part 2, Python: 373 bytes, ~3 s
