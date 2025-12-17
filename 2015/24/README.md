# [2015, Day 24: It Hangs in the Balance](https://adventofcode.com/2015/day/24)


## Solution Notes

A classical Knapsack problem with some minor twists. Not being aware of any efficient algorithms to solve this type of problem and seeing that the problem size is just about feasible, I tried a naive brute-force solution first. That *did* work, but it's excruciatingly slow.

So I did what a programmer has to do in such a situation: read up on a suitable algorithm [on Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem). With this, a solution is produced almost instantly and the code is even a few bytes shorter. (The end result is a tiny bit longer again, but only because I spent the additional 14 bytes to produce the results for both parts.)

In both implementations, I only tried to generate a single knapsack (the "passenger compartment" in the puzzle's nomenclature); a check whether the remaining items are evenly divisible into the 2 or 3 additional buckets is not performed and not necessary. I can't say if I was just lucky with my input or if this is by construction; in any case, the fact that all weights are prime numbers may have something to do with it ...

* Part 1, Python (brute-force): 232 bytes, ~15 min
* Parts 1+2, Python (proper algorithm): 238 bytes, <100 ms
