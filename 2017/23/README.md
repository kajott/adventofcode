# 2017, Day 23: Coprocessor Conflagration


## Solution Notes

Part 1 can be simulated easily using a stripped-down version of the interpreter from [2017 day 18](../18). Part 2, however, would run an (extrapolated estimate) of 28 hours, even when transpiled into C! So there's no way around reverse-engineering the algorithm and finding out that it <span style="background:silver;color:silver;">counts composite (i.e. non-prime) numbers</span>. The only input parameter that varies between AoC users is the very first constant in the code, so it's trivial to extract that and let a significantly more efficient computation run in host code.

* Part 1, Python: 321 bytes, <100 ms
* Part 2, Python: 149 bytes, ~750 ms
