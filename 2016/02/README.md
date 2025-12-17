# [2016, Day 2: Bathroom Security](https://adventofcode.com/2016/day/2)


## Solution Notes

For part 1, I made the choice to not use coordinate system, but simply four translation tables that describe which number shall be mapped to which number under the each of the four translations. This turned out to be the ideal choice, as part 2 is nearly trivial to implement with this.

* Part 1, Python: 161 bytes, <100 ms
* Part 2, Python: 177 bytes, <100 ms
