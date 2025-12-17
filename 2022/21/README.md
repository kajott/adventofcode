# [2022, Day 21: Monkey Math](https://adventofcode.com/2022/day/21)


## Solution Notes

Part 1 is just simple evaluation of the specified operator tree. Nothing to see there.

Part 2 is the interesting one here. In the hope that the correct value is anywhere close to the original value of `humn` (which is in the lower thousands), I tried a brute-force search first, but that obviously led nowhere. The solution really is to invert the equations: The result from the subtree containing `humn` must be equal to the result of the other subtree at the `root` node. With that target value in mind, the next node towards `humn` can be visited, which again has one "fixed" subtree result and a "variable" one (that contains `humn`). The equation can be solved for the required result of the `humn` subtree, which is then used as the target value of that subtree, etc.

All of this is greatly facilitated by the fact that the operator tree is _truly_ a tree, i.e. it's cycle-free, and thus `humn` never occurs in _both_ subtrees of any node. This would have complicated things a lot. Similarly, all multiplications and divisions in the input are designed to be remainder-free; if they weren't, it wouldn't be a simple iterative walk through the tree, but a proper DFS as soon as any division is involved.

The golf solutions for parts 1 and 2 are nearly identical for the part that evaluates a (sub-)tree, hence it was trivial to combine them into a common program. For good measure, I made that (but _only_ that!) Python 3 compatible, even though that cost me a whopping 9 additional bytes.

A few hours later, I learned from a very different approach to solve part 1: Just abuse Python's `exec` function and let it run through the whole input until all variables have been resolved. That's an evil hack if there ever was one, but it *does* the job with very little code, so there's that.

Another novel approach I learned about much later is concerning part 2: Since the operators form a proper tree and all operations are linear, the result must be linear function with respect to the `humn` parameter. Hence, it's sufficient to take two samples (at zero and some large-enough number) and the target value can be computed directly by solving the linear system. Care needs to be taken to do the math with sufficient precision; it worked out for me after a bit of twiddling, but I cant't guarantee that it won't produce off-by-one errors on other inputs. <br>
Anyway, the combined code of this approach is **not** Python 3 compatible, because the overhead of 11 bytes is a bit too much for my taste this time.

* Part 1, Python: 250 bytes, <100 ms
* Part 2, Python (equation inversion): 472 bytes, <100 ms
* Parts 1+2, Python (equation inversion): 492 bytes, <100 ms
* Part 2, Python (linear solver): 318 bytes, <100 ms
* Parts 1+2, Python (linear solver): 330 bytes, <100 ms
* Part 1, Python (evil `exec` hackery): 106 bytes, ~500 ms
