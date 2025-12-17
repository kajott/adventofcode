# 2021, Day 6: Lanternfish


## Solution Notes

Working with a _histogram_ of fish timers instead of the timer list itself not only makes the implementation much easier, it also it essential for part 2. So, if part 1 is already implemented that way, part 2 is really just substituting the constant 80 by 256, without running into any nasty surprises.

* Part 1, Python: 137 bytes, <100 ms
* Part 2, Python: 138 bytes, <100 ms
