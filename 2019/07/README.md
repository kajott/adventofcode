# [2019, Day 7: Amplification Circuit](https://adventofcode.com/2019/day/7)

This puzzle uses the Intcode virtual machine that has been introduced in [days 2](../02) [and 5](../05), and which is going to be used a lot during AoC 2019.

There have been no changes to the Intcode VM since [day 5](../05).

The input for this task consists of an Intcode core dump of (typically) 500 words. The program inputs two numbers, a small integer "phase setting", and an arbitrary integer, called "signal". After processing, it outputs a resulting new "signal" value.

This task is using five independent instances of the Intcode VM, organized in a chain-like structure: the output signal of one instance is the input signal of the next. The first instance's input signal is zero. The "phase setting" values for each instance are unspecified, but they must be some permutation of the valid number range (which differs between parts).

**Part 1** asks for the highest final output signal across all possible "phase setting" permutations with values 0-4.

**Part 2** asks the same, but with the VMs arranged in a feedback loop that sends the last machine's output signal back to the first machine's input signal, and with "phase setting" values of 5-9. In these modes, the programs run a loop that requests input signals and produces output signals multiple times, until they eventually terminate.


## Solution Notes

One of the puzzles that just need to be coded down without requiring any special ideas. Python's `itertools.permutations` function is a key asset here.

* Part 1, Python: 462 bytes, ~150 ms
* Part 2, Python: 603 bytes, ~150 ms
