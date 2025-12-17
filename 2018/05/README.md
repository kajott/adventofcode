# [2018, Day 5: Alchemical Reduction](https://adventofcode.com/2018/day/5)


## Solution Notes

My initial implementation (and seemingly the ones from many other participants as well) actually performed a repeated reaction until the polymer string didn't change. That's fine, but also really slow -- the solution for part 2 took almost a minute to compute.

In the end, I found out that the reduction can be done in a single pass -- you just need to go back one additional position after removing a reacting pair of units! This makes the code more than an order of magnitude faster, as can be seen in my implementations: part 1 still uses the repeated partial reaction algorithm, while part 2 performs 26 iterations of the faster algorithm, and is still twice as fast.

* Part 1, Python (multi-pass): 181 bytes, ~4 s
* Part 2, Python (single-pass): 260 bytes, ~2 s
