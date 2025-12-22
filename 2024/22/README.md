# [2024, Day 22: Monkey Market](https://adventofcode.com/2024/day/22)

The input contains (typically) 2400 24-bit numbers.

A PRNG / hash function is defined that maps a 24-bit number to another.

**Part 1** asks to run the PRNG function 2000 times on each of the input numbers (seeds).

In **part 2**, only the last (decimal) digit of the number sequences play a role, and in particular the _deltas_ between successive iterations. The task is to find the sequence of four deltas that maximizes the last digit of the PRNG sequence at the point right before the delta sequence, across all seeds.


## Solution Notes

The most complex thing about this puzzle is understanding the task description. For starters, all those multiplications, divisions and modulos amount to simple shifts and ANDs, and the entire thing is just a 24-bit [XORshift](https://en.wikipedia.org/wiki/Xorshift) PRNG. Part 1 is just about implementing that and letting it run for ~4 million iterations (~2k input lines x 2k iterations per line). CPython is surprisingly slow at this and there's nothing that can be done to optimize it further; just using PyPy gives the answer in a fraction of a second.

Part 2 boils down to observing the previous 4 values modulo 10 and their deltas while perfoming the 2k PRNG iterations per line. Each time a sequence of 4 deltas occurs for the first time for an input line, the current value (modulo 10) can be added to the achievable score for that delta sequence. After all the input lines have been processed, the highest such score across all sequences is the result.

Due to all the dictionary manipulation involved, part 2 is no longer significantly faster on PyPy than on CPython. But how fast could it be? Out of curiosity, I implemented a C version of this puzzle, using a flat zero-initialized list instead of hash maps for the central data structure. After all, there are just 19^4 = ~130k possible sequences of four deltas, and not even all of these are valid (9,9,9,9, for example, isn't), so the entire thing fits comfortably into a modern CPU's cache. There only need to be two data items per entry: The resulting score, and some kind of flag to note whether this delta sequence has already been encountered for the current line. Since I didn't want to waste any time on clearing this flag, I opted for a line counter instead: An entry is only updated if it hasn't been updated already for the current input line. The solution is even relatively nicely golfable, coming in at well below 500 bytes, and it executes practically instantaneously, even if the compile time is included.

* Part 1, Python: 120 bytes, ~2.5 s
* Part 2, Python: 238 bytes, ~10 s
* Parts 1+2, C: 451 bytes, ~150 ms
