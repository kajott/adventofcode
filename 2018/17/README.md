# [2018, Day 17: Reservoir Research](https://adventofcode.com/2018/day/17)


## Solution Notes

The rules are moderately easy to understand, but the details are hard to get right in practice. My initial approach was to perform a "drop-by-drop" simulation of the water flow, which is a dead end. A slightly smarter algorithm that follows the water downward to the closest ground and spills whole rows there is much more efficient.

As the difference between the solutions for parts 1 and 2 would really just be a single byte, I didn't bother to generate separate implementations. Instead, the one program here generates the answers for both parts. As a bonus, there's a simple visualization script that renders the final water map into a `ppm` file.

* Parts 1+2, Python: 725 bytes, ~2 s
