# [2022, Day 11: Monkey in the Middle](https://adventofcode.com/2022/day/11)

The input consists of a description of (typically) 7 agents ("monkeys") with the following properties:
- starting items: 1 to 8 2-digit numbers
- operation: either an increment by a constant, multiplication by a constant, or squaring
- test: divisible by some constant
- branching instructions that describe to which monkey to "throw" to if the test succeeds and fails

At each round, each monkey processes the numbers they currently have, in order. For each number, two operations are performed: the operation described in the input, and a floor division by three. Then, the divisibility test is performed and the number is sent to the queue of the target monkey. It does not become active until the next round.

**Part 1** asks to simulate 20 rounds and trace, for each monkey, how many items (numbers) have been processed.

**Part 2** asks the same, but for **10,000** rounds.


## Solution Notes

Part 1 is mostly about writing a parser to interpret the relatively complex input syntax, and then implement the rules in a straight-forward way. Shortcuts can be made; in particular, abusing the `eval()` function to compute the result of the value formula is a popular one.

Part 2 is a completely different beast, a textbook example of the "complexity explodes, find your way out" type of puzzle. In this case, the solution is running all computations modulo the GCD of the "divisibly by" checks of all monkeys. (Since all those values are coprime, and small, the product works too.) There may be further optimizations possible, but this one already pushes the runtime into the realm of the reasonable, so let's keep it at that.

* Part 1, Python: 325 bytes, <100 ms
* Part 2, Python: 343 bytes, ~3.5 s
