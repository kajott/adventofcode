# 2023, Day 12: Hot Springs


## Solution Notes

Part 1 can be solved by brute force, but it's unwieldy; I get a runtime of well above 10 seconds, and the code isn't particularily elegant either.

Part 2 is where brute force really falls apart, as complexity is raised to a power of 5, times 16. Another approach is required that intelligently only checks combinations that are possible at all (for example, it doesn't make sense to add any `#`s if all the desired runs are exhausted already), and uses caching to not revisit states that have already been analyzed. With those two elements under the belt, part 2 only takes a little over a second here (the golf version is 2x slower; replace the `*` in line 9 by `and` to reinstate full performance), and the code is even smaller to boot!

* Part 1, Python (brute force): 365 bytes, ~20 s
* Part 1, Python (approach from part 2): 323 bytes, ~100 ms
* Part 2, Python: 339 bytes, ~3 s
