# 2024, Day 7: Bridge Repair

The Historians take you to a familiar [rope bridge](../../2022/09) over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and _stole all the operators_ from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

## Part 1

For example:

    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are _always evaluated left-to-right_, _not_ according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: _add_ (`+`) and _multiply_ (`*`).

Only three of the above equations can be made true by inserting operators:

*   `190: 10 19` has only one position that accepts an operator: between `10` and `19`. Choosing `+` would give `29`, but choosing `*` would give the test value (`10 * 19 = 190`).
*   `3267: 81 40 27` has two positions for operators. Of the four possible configurations of the operators, _two_ cause the right side to match the test value: `81 + 40 * 27` and `81 * 40 + 27` both equal `3267` (when evaluated left-to-right)!
*   `292: 11 6 16 20` can be solved in exactly one way: `11 + 6 * 16 + 20`.

The engineers just need the _total calibration result_, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is _`3749`_.

Determine which equations could possibly be true. _What is their total calibration result?_

Your puzzle answer was `7885693428401`.

## Part 2

The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a _third type of operator_.

The [concatenation](https://en.wikipedia.org/wiki/Concatenation) operator (`||`) combines the digits from its left and right inputs into a single number. For example, `12 || 345` would become `12345`. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

*   `156: 15 6` can be made true through a single concatenation: `15 || 6 = 156`.
*   `7290: 6 8 6 15` can be made true using `6 * 8 || 6 * 15`.
*   `192: 17 8 14` can be made true using `17 || 8 + 14`.

Adding up all six test values (the three that could be made before using only `+` and `*` plus the new three that can now be made by also using `||`) produces the new _total calibration result_ of _`11387`_.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. _What is their total calibration result?_

Your puzzle answer was `348360680516005`.

## Solution Notes

This boils down to a DFS-like recursive algorithm that receives the current value and the next operands, tries all possible operators and returns a set of possible results; at least, that was my initial implementation. For golfing purposes _and_ runtime efficiency, it turned out to be beneficial to have the function perform the checking itself too: It receives the expected test value as an additional parameter and returns either that if it found a solution, or zero if it didn't.

To little surprise, part 2 takes substantially longer to compute than part 1. Not only is 3<sup>n</sup> much more than 2<sup>n</sup>; the integer-to-string-and-back roundtrip used for the concatenation operation also isn't cheap. There are plenty of ways to optimize things though: First, there's no need to try further operations when a result has been found; second, since all operations only cause the numbers to grow, recursion can stop if the current value is already larger than the test value; and third, the string conversion roundtrip can be replaced with a multiplication by a power of 10 based on the value of the second operand. I implemented the first two strategies in my code and also got rid of my golf-induced abuse of `*args` to get a decent ~4x speedup; the last strategy is not at all conductive to code golf, so I stopped at that point.

* Part 1, Python: 148 bytes, ~150 ms
* Part 2, Python (naive): 182 bytes, ~7 s
* Part 2, Python (optimized): 209 bytes, ~2 s
