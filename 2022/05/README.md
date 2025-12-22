# [2022, Day 5: Supply Stacks](https://adventofcode.com/2022/day/5)

The input consists of a description of the initial state of (typically) 9 stacks, each containing 3-8 objects named by a single letter each. In addition, there are (typically) 500 instructions about how many objects to move from which stack to which other stack.

Even though multiple objects can be moved in a single instruction, the objects are still moved one after the other, i.e. they will arrive at their destination in reversed order.

**Part 1** asks for the object names at the top of each stack after the instructions have been executed.

**Part 2** asks the same, but this time, multiple objects do **not** reverse their order while being moved.


## Solution Notes

This is one of the puzzles where the task itself is nearly trivial, but parsing the input and picking a suitable representation for the data is where the (still not too excessive) complexity lies.

After several rounds of miniaturization, I ended up in a state where part 2 is actually shorter than part 1, simply because the order of the moved elements is reversed in part 1, while it's kept intact in part 2.

* Part 1, Python: 282 bytes, <100 ms
* Part 2, Python: 276 bytes, <100 ms
