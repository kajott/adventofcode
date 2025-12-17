# [2015, Day 25: Let It Snow](https://adventofcode.com/2015/day/25)


## Solution Notes

The (slightly) hard part of this puzzle is determining the ordinal number for the specified coordinates. This turns out to be quite simple; it even has a closed-form solution, exploiting the fact that the first numbers for each successive diagonal are the sum of the first _n_ natural numbers plus 1, i.e. `(n²+n)/2+1`. All that remains is running the [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator) the appropriate number of times (which is quite staggering: almost 20 million).

* Part 1, Python: 145 bytes, ~3 s
