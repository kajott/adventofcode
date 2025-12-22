# [2024, Day 7: Bridge Repair](https://adventofcode.com/2024/day/7)

The input consists of (typically) 850 "equations", each consisting of 5 to 12 single-digit to 3-digit numbers and a 4-to-12-digit result.

**Part 1** asks how which equations can be made true by performing additions or multiplications between the numbers, disregarding operator precedent.

**Part 2** asks the same, but with a third possible operator: number-as-string concatenation.


## Solution Notes

This boils down to a DFS-like recursive algorithm that receives the current value and the next operands, tries all possible operators and returns a set of possible results; at least, that was my initial implementation. For golfing purposes _and_ runtime efficiency, it turned out to be beneficial to have the function perform the checking itself too: It receives the expected test value as an additional parameter and returns either that if it found a solution, or zero if it didn't.

To little surprise, part 2 takes substantially longer to compute than part 1. Not only is 3<sup>n</sup> much more than 2<sup>n</sup>; the integer-to-string-and-back roundtrip used for the concatenation operation also isn't cheap. There are plenty of ways to optimize things though: First, there's no need to try further operations when a result has been found; second, since all operations only cause the numbers to grow, recursion can stop if the current value is already larger than the test value; and third, the string conversion roundtrip can be replaced with a multiplication by a power of 10 based on the value of the second operand. I implemented the first two strategies in my code and also got rid of my golf-induced abuse of `*args` to get a decent ~4x speedup; the last strategy is not at all conductive to code golf, so I stopped at that point.

* Part 1, Python: 148 bytes, ~250 ms
* Part 2, Python (naive): 182 bytes, ~15 s
* Part 2, Python (optimized): 209 bytes, ~3.5 s
