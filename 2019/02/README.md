# [2019, Day 2: 1202 Program Alarm](https://adventofcode.com/2019/day/2)


## Solution Notes

Part 1 is a straightforward emulation puzzle, though with a von Neumann architecture this time. Part 2 looks like something that would require reverse engineering at first, but the program is simple enough that brute-forcing through all 10000 verb/noun combinations is fine. I feel a bit bad for re-opening and re-reading the input 10k times in my solution, but it's still fast enough and saves a few bytes, so there's no reason to change it.

* Part 1, Python: 149 bytes, <100 ms
* Part 2, Python: 197 bytes, ~600 ms
