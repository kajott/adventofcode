# [2021, Day 14: Extended Polymerization](https://adventofcode.com/2021/day/14)

The input consists of a random (typically) 20-character string, and a list of (typically) 100 mappings of two characters to a single character.

At each time step, for each pair of characters in the string, the associated character from the map is inserted between the characters of the original pair.

**Parts 1 and 2** ask to simulate 10 and 40 time steps, respectively.


## Solution Notes

Part 1 is solvable in the straightforward way; for part 2, it's required to recognize that the only required information to keep track of is a histogram _of pairs_ of elements.

* Part 1, Python: 233 bytes, <100 ms
* Part 2, Python: 375 bytes, <100 ms
