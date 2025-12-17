# [2018, Day 19: Go With The Flow](https://adventofcode.com/2018/day/19)


## Solution Notes

This is one of the puzzles where part 1 is a simple simulation (that nevertheless runs quite long) and part 2 cranks up the problem size into ridiculous territory. The twist here is that you really need to understand what the program does, either by watching it work or plain reverse engineering it. I chose the first approach: tracing all writes to the result register reveals that the code is gradually adding numbers to it. The pattern wasn't clear at first, but it turns out to be a simple <span style="color:silver;background:silver;">sum-of-divisors</span> computation. The input parameter of this is kept in a register all the time, so my solution is to let the simulation run for a few dozen cycles to let it compute the parameter, grab that from the register bank (it's generally the largest value), and perform the actual computation in host code. With this trick, part 2 actually runs faster than a plain simulation of part 1, and part 1 would run in less than 30 milliseconds. The main computation could be optimized further, but at that point, I didn't bother.

Note that this puzzle isn't really amenable to code golf, since the opcodes need to be declared somewhere, which takes up more than half of the whole program size.

* Part 1, Python (plain simulation): 661 bytes, ~3 s
* Part 2, Python (host computation): 704 bytes, ~1 s
