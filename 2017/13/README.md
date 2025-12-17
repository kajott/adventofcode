# [2017, Day 13: Packet Scanners](https://adventofcode.com/2017/day/13)


## Solution Notes

The obvious way to solve this is to perform a full simulation of all scanner positions. This isn't necessary though, as they move regularly and a stateless solution can be found that computes the scanner position at any point in time. This makes the code much more compact.

For part 2, I just did a brute-force simulation of all delay values. Even though the answer is well into the millions, this is fast enough to be reasonable.

* Part 1, Python: 149 bytes, <100 ms
* Part 2, Python: 167 bytes, ~5 s
