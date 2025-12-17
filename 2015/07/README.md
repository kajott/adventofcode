# 2015, Day 7: Some Assembly Required


## Solution Notes

A nice straightforward ~~simulation~~ evaluation puzzle, the only caveat of which is that a cache for already evaluated wires is required to get acceptable performance.

In the golf version, I tried to define the operators as `lambda`s in a dictionary, but a plain `if` cascade turned out to be smaller than that. It also doesn't make much sense to split the implementation into two parts, as the only major difference is an additional line for part 2.

* Parts 1+2, Python: 419 bytes, <100 ms
