# 2023, Day 19: Aplenty


## Solution Notes

The parser is a bit convoluted, but other than that, part 1 doesn't have anything worth talking about.

Part 2 seems to be a tall order again, but it's actually quite tame: Starting with a single 4000^4 hypercube, every (sub-)rule divides it along one of the axes, and the next rule divides it again, etc., until `A` or `R` is reached. Care needs to be taken to get the conditions exactly right; a popular mistake is to properly treat the case where the variable's value is _equal_ to the reference value.

* Part 1, Python: 434 bytes, <100 ms
* Part 2, Python: 525 bytes, <100 ms
