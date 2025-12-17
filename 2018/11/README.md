# [2018, Day 11: Chronal Charge](https://adventofcode.com/2018/day/11)


## Solution Notes

This is one of the "hah, your naive solution won't scale for part 2" puzzles. Indeed, my first approach runs almost 10 minutes in total, though the correct result is already produced after little more than 2 seconds -- but what if a there's a better result at a larger summation size? (It's unlikely, as the overall matrix has a small negative bias, favoring smaller summations, but you can't be sure.)

The first optimization step is to pre-compute a matrix with NxN sub-square sums for each size and then finding the maximum. This already reduced the computation time to 3% of the initial approach for me. But the pre-computation itself was still implemented in a naive manner, so I optimized this again and got down to less than five seconds for the full solution in Python.

An alternate solution is making use of a [summed-area table](https://en.wikipedia.org/wiki/Summed-area_table), and this is indeed the optimal approach in terms of code size and performance.

In C, I got the two fastest Python implementations down to less than 100 milliseconds each on a fast machine, *including* compilation. (Without that, the SAT solution takes are mere 20 milliseconds to run on said machine.) This time, compiler optimization was a net win, i.e. it makes the code so much faster (~3x) that the longer compile times are more than compensated.

* Part 1, Python: 201 bytes, ~150 ms
* Part 2, Python (naive): 260 bytes, ~10 minutes
* Part 2, Python (pre-summed matrix): 305 bytes, ~25 s
* Part 2, Python (optimized pre-summed matrix): 361 bytes, ~6 s
* Part 2, Python (SAT): 303 bytes, ~3.5 s
* Part 2, C (optimized pre-summed matrix): 442 bytes, ~150 ms
* Part 2, C (SAT): 381 bytes, ~150 ms
