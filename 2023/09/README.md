# [2023, Day 9: Mirage Maintenance](https://adventofcode.com/2023/day/9)

The input consists of (typically) 200 series of (typically) 21 signed numbers in the 1-to-8-digit range.

**Part 1** asks to extrapolate an extra value at the end of each series by performing repeated pairwise differentiation and, once all differences are zero, integration to construct the extra value.

**Part 2** asks to extrapolate an extra value at the _beginning_ of each series with the same approach.


## Solution Notes

Just do exactly as described, and you'll get the result. I was only stuck for a minute when I accidentally carried out the subtractions in reverse order in part 2, but that was easy to solve.

* Part 1, Python: 154 bytes, <100 ms
* Part 2, Python: 180 bytes, <100 ms
