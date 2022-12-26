# 2022, Day 21: Monkey Math

The [monkeys](../11) are back! You're worried they're going to try to steal your stuff again, but it seems like they're just holding their ground and making various monkey noises at you.

Eventually, one of the elephants realizes you don't speak monkey and comes over to interpret. As it turns out, they overheard you talking about trying to find the grove; they can show you a shortcut if you answer their _riddle_.

## Part 1

Each monkey is given a _job_: either to _yell a specific number_ or to _yell the result of a math operation_. All of the number-yelling monkeys know their number from the start; however, the math operation monkeys need to wait for two other monkeys to yell a number, and those two other monkeys might _also_ be waiting on other monkeys.

Your job is to _work out the number the monkey named `root` will yell_ before the monkeys figure it out themselves.

For example:

    root: pppw + sjmn
    dbpl: 5
    cczh: sllz + lgvd
    zczc: 2
    ptdq: humn - dvpt
    dvpt: 3
    lfqf: 4
    humn: 5
    ljgn: 2
    sjmn: drzm * dbpl
    sllz: 4
    pppw: cczh / lfqf
    lgvd: ljgn * ptdq
    drzm: hmdt - zczc
    hmdt: 32
    

Each line contains the name of a monkey, a colon, and then the job of that monkey:

*   A lone number means the monkey's job is simply to yell that number.
*   A job like `aaaa + bbbb` means the monkey waits for monkeys `aaaa` and `bbbb` to yell each of their numbers; the monkey then yells the sum of those two numbers.
*   `aaaa - bbbb` means the monkey yells `aaaa`'s number minus `bbbb`'s number.
*   Job `aaaa * bbbb` will yell `aaaa`'s number multiplied by `bbbb`'s number.
*   Job `aaaa / bbbb` will yell `aaaa`'s number divided by `bbbb`'s number.

So, in the above example, monkey `drzm` has to wait for monkeys `hmdt` and `zczc` to yell their numbers. Fortunately, both `hmdt` and `zczc` have jobs that involve simply yelling a single number, so they do this immediately: `32` and `2`. Monkey `drzm` can then yell its number by finding `32` minus `2`: _`30`_.

Then, monkey `sjmn` has one of its numbers (`30`, from monkey `drzm`), and already has its other number, `5`, from `dbpl`. This allows it to yell its own number by finding `30` multiplied by `5`: _`150`_.

This process continues until `root` yells a number: _`152`_.

However, your actual situation involves considerably more monkeys. _What number will the monkey named `root` yell?_

Your puzzle answer was `80326079210554`.

## Part 2

Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.

First, you got the wrong job for the monkey named `root`; specifically, you got the wrong math operation. The correct operation for monkey `root` should be `=`, which means that it still listens for two numbers (from the same two monkeys as before), but now checks that the two numbers _match_.

Second, you got the wrong monkey for the job starting with `humn:`. It isn't a monkey - it's _you_. Actually, you got the job wrong, too: you need to figure out _what number you need to yell_ so that `root`'s equality check passes. (The number that appears after `humn:` in your input is now irrelevant.)

In the above example, the number you need to yell to pass `root`'s equality test is _`301`_. (This causes `root` to get the same number, `150`, from both of its monkeys.)

_What number do you yell to pass `root`'s equality test?_

Your puzzle answer was `3617613952378`.

## Solution Notes

Part 1 is just simple evaluation of the specified operator tree. Nothing to see there.

Part 2 is the interesting one here. In the hope that the correct value is anywhere close to the original value of `humn` (which is in the lower thousands), I tried a brute-force search first, but that obviously led nowhere. The solution really is to invert the equations: The result from the subtree containing `humn` must be equal to the result of the other subtree at the `root` node. With that target value in mind, the next node towards `humn` can be visited, which again has one "fixed" subtree result and a "variable" one (that contains `humn`). The equation can be solved for the required result of the `humn` subtree, which is then used as the target value of that subtree, etc.

All of this is greatly facilitated by the fact that the operator tree is _truly_ a tree, i.e. it's cycle-free, and thus `humn` never occurs in _both_ subtrees of any node. This would have complicated things a lot. Similarly, all multiplications and divisions in the input are designed to be remainder-free; if they weren't, it wouldn't be a simple iterative walk through the tree, but a proper DFS as soon as any division is involved.

The golf solutions for parts 1 and 2 are nearly identical for the part that evaluates a (sub-)tree, hence it was trivial to combine them into a common program. For good measure, I made that (but _only_ that!) Python 3 compatible, even though that cost me a whopping 9 additional bytes.

A few hours later, I learned from a very different approach to solve part 1: Just abuse Python's `exec` function and let it run through the whole input until all variables have been resolved. That's an evil hack if there ever was one, but it *does* the job with very little code, so there's that.

Another novel approach I learned about much later is concerning part 2: Since the operators form a proper tree and all operations are linear, the result must be linear function with respect to the `humn` parameter. Hence, it's sufficient to take two samples (at zero and some large-enough number) and the target value can be computed directly by solving the linear system. The math is a bit shaky though: I only managed to get stable results on my and the example inputs on Python 2 and with a very specific combination of floating-point and integer arithmetic; otherwise, off-by-one errors occur. That's why the combined solution for this approach is, again, Python 2 only.

* Part 1, Python: 250 bytes, <100 ms
* Part 2, Python (equation inversion): 472 bytes, <100 ms
* Parts 1+2, Python (equation inversion): 492 bytes, <100 ms
* Part 2, Python (linear solver): 318 bytes, <100 ms
* Parts 1+2, Python (linear solver): 329 bytes, <100 ms
* Part 1, Python (evil `exec` hackery): 106 bytes, ~500 ms
