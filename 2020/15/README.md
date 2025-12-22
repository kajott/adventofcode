# [2020, Day 15: Rambunctious Recitation](https://adventofcode.com/2020/day/15)

The input consists of (typically) 7 1-to-2-digit numbers.

The list of numbers is extended by one item at a time using the following rule: The last number in the list is examined. If this is the only occurrence of that number in the list, a zero is appended. Otherwise, the difference in index between the last two occurrences is appended.

**Part 1** asks for the 2020th number.

**Part 2** asks for the number at index 30 million.


## Solution Notes

A simple "implement the rules and let it run" puzzle, but a little pitfall is that the fules must really be followed to the letter to get the proper results.

Part 2 is extremely strange: It increases the problem size into the territory where there's usually some periodic property of the puzzle that has to be exploited to be even remotely efficient. Not so this time: The ouput is pretty chaotic, there is no short circuit. You just have to wait until the result is ready.

A C implementation (which is a very simple golfing exercise, by the way) is again 10x faster. This number includes compilation, but this time, compilation takes only a negligible amount of time.

* Part 1, Python: 112 bytes, <100 ms
* Part 2, Python: 116 bytes, ~15 s
* Part 2, C: 223 bytes, ~1.5 s
