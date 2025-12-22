# [2023, Day 19: Aplenty](https://adventofcode.com/2023/day/19)

The input consists of a (typically) 200 4D 2-to-4-digit coordinates and a list of (typically) 550 named processing rules. Each rule contains a list of comparisons, and a fallback rule that shall be used if none of the comparisons matched. Each comparison compares one of the coordinates against a constant and continues to some other rule if the result is true. There is one specially-named rule where processing starts. Two special pseudo-rules terminate the comparison process with an "accept" or "reject" result.

**Part 1** asks which of the coordinates would be accepted after running the comparison process.

**Part 2** asks for the volume of the 4D hypercuboid that would be accepted.


## Solution Notes

The parser is a bit convoluted, but other than that, part 1 doesn't have anything worth talking about.

Part 2 seems to be a tall order again, but it's actually quite tame: Starting with a single 4000^4 hypercube, every (sub-)rule divides it along one of the axes, and the next rule divides it again, etc., until `A` or `R` is reached. Care needs to be taken to get the conditions exactly right; a popular mistake is to properly treat the case where the variable's value is _equal_ to the reference value.

* Part 1, Python: 434 bytes, <100 ms
* Part 2, Python: 525 bytes, <100 ms
