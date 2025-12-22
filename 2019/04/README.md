# [2019, Day 4: Secure Container](https://adventofcode.com/2019/day/4)

The input consists of a single range of 6-digit numbers. Withing this range, numbers shall be searched that have any digit repeating at least twice in succession, and that have all digits in monotonically increasing order.

**Part 1** asks for the total count of numbers that fulfill these criteria.

**Part 2** asks the same, but with the repeating digit rule changed from "at least two repetitions" to "exactly two repetitions".


## Solution Notes

A relatively simple task that is best done by converting the numbers to strings and operating on these. Minifying the code was quite fun, and I ended up with only minimally different oneliners for both parts, but that came at the expense of performance.

* Part 1, Python: 121 bytes, ~1 s
* Part 2, Python: 122 bytes, ~1 s
