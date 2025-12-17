# 2017, Day 17: Spinlock


## Solution Notes

Part 2 of this puzzle requires two "heureka" moments to be solved.

First, I noticed that simply abusing an array like a Python `list` won't cut it because of the O(n) insertion time. So I went for an implementation that uses proper single-linked circular list structures.

However, these implementations -- even the one in C! -- were still unreasonably slow, at least for the puzzle input I got; with the example value of 3, everything's quite snappy. That's because walking through the list, 300-ish steps times 50 million iterations, is pure poison for the CPU cache.

I should have been suspicious of why part 2 doesn't ask for the same information as part 1, because that's what gives the eventual solution away: _A full representation of the list's contents isn't required for part 2._ All that's needed is tracking the current position, the position of value zero, and write operations to the index _after_ value zero. This makes for a very compact implementation, even though the runtime performance is still nothing to write home about.

* Part 1, Python (full simulation with arrays): 80 bytes, <100 ms
* Part 2, Python (full simulation with circular list): 136 bytes, ~10 hours (estimated), ~20 GB of RAM
* Part 2, C (full simulation with circular list): 299 bytes, ~8 min
* Part 2, Python (tracking): 90 bytes, ~12 s
