# [2020, Day 12: Rain Risk](https://adventofcode.com/2020/day/12)

The input consists of (typically) 790 motion instructions, each consisting of a direction and a 1-to-3-digit distance. The directions can be to rotate left or right in 90-degree steps and moving forward, but they can _also_ be direct motion in any of the four cardinal directions, not changing the heading of the player.

**Part 1** asks for the player position after executing the instructions.

**Part 2** asks the same, but this time, not the player itself is controlled by the instructions, but a direction vector that's always relative to the player position. Cardinal direction motion only modifies the vector, rotation rotates the vector around the current player position, and the "forward" direction actually moves the player by the vector, multiplied by the distance.


## Solution Notes

As straightforward as it gets: Follow the instructions, and done. When golfing, the main loop can be done on a single (lengthy) line. Just don't make the same error as I did and ignore the argument to the `L`/`R` operations -- there _are_ indeed 180-degree and 270-degree rotations in the input, not just 90 degrees ...

* Part 1, Python: 177 bytes, <100 ms
* Part 2, Python: 191 bytes, <100 ms
