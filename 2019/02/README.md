# [2019, Day 2: 1202 Program Alarm](https://adventofcode.com/2019/day/2)

This puzzle introduces the Intcode virtual machine that's going to be used a lot during AoC 2019.

Intcode operates on memory of unspecified word size that contains both the program code and data. There are no registers, data is stored exclusively in memory. The following operations are supported:
- `1,a,b,d` = add: `mem[d] = mem[a] + mem[b]`
- `2,a,b,d` = multiply: `mem[d] = mem[a] * mem[b]`
- `99` = stop execution

The input for this task consists of an Intcode core dump of (typically) 120 words.

In this task, two specific memory addresses are designated to hold a "verb" and a "noun", respectively. Both are values between 0 and 99. The program is performing some computations on them and outputs its result at address 0.

**Part 1** asks for the result of running the program for a specifc verb/noun combination.

**Part 2** asks for the verb/noun combination that produces a specific result.


## Solution Notes

Part 1 is a straightforward emulation puzzle, though with a von Neumann architecture this time. Part 2 looks like something that would require reverse engineering at first, but the program is simple enough that brute-forcing through all 10000 verb/noun combinations is fine. I feel a bit bad for re-opening and re-reading the input 10k times in my solution, but it's still fast enough and saves a few bytes, so there's no reason to change it.

* Part 1, Python: 149 bytes, <100 ms
* Part 2, Python: 197 bytes, ~600 ms
