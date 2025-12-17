# [2018, Day 4: Repose Record](https://adventofcode.com/2018/day/4)


## Solution Notes

The most complex task in this puzzle is converting the input into nice (guard ID, sleep start, sleep end) tuples. I did this by combining the full timestamp into a single `MMDDHHMM` decimal number (the year is always the same, so that can be ignored). Then all events are sorted by this timestamp. It turned out that the input is well-formed enough to disregard the date and time of the "guard begins shift" events -- I just make a note that all following sleep/wake-up events belong to the specified guard. At this point, only the minutes part of the timestamp is used, as the solution doesn't care about absolute times (all it needs is a histogram of sleep times relative to midnight), and the hour is always zero anyway.

The funny thing is how similar parts 1 and 2 are: In my implementation, I just had to change a `sum` into a `max`, and that was it!

* Part 1, Python: 359 bytes, <100 ms
* Part 2, Python: 359 bytes, <100 ms
