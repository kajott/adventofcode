# [2019, Day 17: Set and Forget](https://adventofcode.com/2019/day/17)

This puzzle uses the Intcode virtual machine that has been fully specified in [day 9](../09), and which is going to be used a lot during AoC 2019.

The input for this task consists of an Intcode core dump of (typically) 1450 words.

The program generates an ASCII map of a single self-intersecting path on a (typically) 50x40 grid,

**Part 1** asks to identify all intersections in that path.

The objective of **part 2** is to provide the program with instructions to walk the entire path from start to end. Individual Instructions can be either `L` or `R` for turns, or a number for moving forwards; multiple instructions are joined with commas. However, the instructions can be at most 20 characters long. To overcome this limitation, subsequences of (again, at most 20) characters can be stored into three subprograms `A`, `B` and `C`, which can then be called from the main program like any normal instruction.

**Part 2** asks for the result produced by the Intcode program after successfully walking the entire path.


## Solution Notes

Part 1 is just a simple introduction into the task; nothing to write home about.

Part 2 is where the meat is. Fortunately, the inputs are constructed in a way that makes a few simplifications possible which aren't necessarily clear from the task description. There are five things that need to be done:

1. Run the program to get the ASCII map.

2. Parse the map, extract the locations of the scaffold path, and the robot's starting location and heading. As is turns out, the initial heading is always north (`^`), a fact that I happily made use of in the golf implementation.

3. Generate the raw instructions for traversing the scaffold. It's always a single path that doesn't bifurcate, and the starting position is at one end of the path, so there's no need to backtrack at any point. The sequence thus contains alternating turn and run commands, which can be grouped together into "packets" like `L,4` or `R,10`. Furthermore, the scaffold where the robot starts is always oriented in east-west direction, even though the robot starts facing north, so the sequence always starts with a full packet containing an `L` or `R`.

4. Split the sequence into a pattern that references up to three subsequences, obeying the 20-character length limits. This is pretty much what a Lempel-Ziv-based data compressor would do, except that the constraints force a so-called "optimal parse"; simple greedy matching will not suffice. I used a DFS for that, but there may be other approaches. The good news is that the puzzle input is constructed such that it's never necessary to split runs, i.e. just working on the "packets" generated in step 3 is sufficient.

5. Compile the final commands, send them into the program and receive the final map and the result value.

All this adds up to a significant amount of code that's not very amenable to golfing, hence I ended up with well above a kilobyte for part 2 (including the Intcode interpreter).

* Part 1, Python: 546 bytes, ~250 ms
* Part 2, Python: 1128 bytes, ~500 ms
