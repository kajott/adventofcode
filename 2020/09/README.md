# [2020, Day 9: Encoding Error](https://adventofcode.com/2020/day/9)

The input consists of (typically) 1000 numbers, starting at 1 to 2 digits, and growing in magnitude up to 14 digits.

The numbers are supposed to form a sequence where every number should be the sum of any two other numbers in the 25 slots preceding it.

**Part 1** asks for the first number in the sequence that does _not_ follow this constraint.

**Part 2** asks to find a continuous run of numbers in the sequence that sums up to the number found in part 1.


## Solution Notes

The sheer number of combinations that need to be tested for a brute-force solution might sound high at first, but it's in fact much less than a million combinations in total, so even though we're dealing with O(n^3) here, it's not really an issue.

As the problem description already states, part 2 is (almost) a true superset of part 1. (In fact, a combined solution would just use an additional `print` statement.)

* Part 1, Python: 144 bytes, ~150 ms
* Part 2, Python: 227 bytes, ~250 ms
