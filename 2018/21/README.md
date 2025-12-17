# [2018, Day 21: Chronal Conversion](https://adventofcode.com/2018/day/21)


## Solution Notes

Yet another reverse engineering puzzle, flavored with infuriatingly misleading wording in the questions.

In the end, it boils down to first find out what the program actually does with register `0`. In this case, it generates a sequence of numbers, compares it to the register, and terminates if it matches. So, for the first part of the puzzle, it's all about letting it run until the first such comparison, and noting the value of the reference register.

For part 2, the task is to find out that the sequence repeats and answer with the last reference value *before* the cycle. This can be done in simulation too, but it takes minutes to compute the necessary 10k-ish iterations.

The more elegant (yet hacky) solution is thus to reverse-engineer the algorithm (which is a variant of <span style="color:silver;background:silver;">a linear congruential pseudo-random number generator</span>) and run it at native speed, which is what I did. It just grabs the user-specific parameter from the input file (under the assumption that it's within a reasonably large range), and then goes on to produce the result in a blink of an eye and in a "tweetable" amount of code.

* Part 1, Python (host computation): 130 bytes, <100 ms
* Part 2, Python (host computation): 195 bytes, <100 ms
