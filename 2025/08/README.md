# [2025, Day 8: Playground](https://adventofcode.com/2025/day/8)


## Solution Notes

This task calls for some creative use of dictionaries and sets. First, a full distance matrix has to be computed and sorted (which takes surprisingly long, by the way), and then, the connections can be made. To keep track of those, I used a dictionary containing the circuit (as a set) where each box belongs into. Multiple entries in there will have the same value, and that's fine. At the end, it boils down to identifying distinct circuits.

The solution isn't perfectly amenable to code golf. It's also one of the cases where part 2 is actually shorter than part 1, as the entire evaluation step is skipped.

* Part 1, Python: 290 bytes, ~1.5 s
* Part 2, Python: 255 bytes, ~2.5 s
