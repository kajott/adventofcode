# [2019, Day 21: Springdroid Adventure](https://adventofcode.com/2019/day/21)

This puzzle uses the Intcode virtual machine that has been fully specified in [day 9](../09), and which has been used a lot during AoC 2019.

The input for this task consists of an Intcode core dump of (typically) 2050 words.

The task is about simple jumping game (similar to Google Chrome's offline dinosaur game) where the character controller by the player needs to jump at proper intervals. The game is simulated on a fixed integer grid. There are no obstacles, only holes in the ground.

The simulation of the game runs inside the Intcode VM. In contrast to [day 13](../13), the inputs are not directly provided to the Intcode program; instead, the VM runs *another* nested virtual machine. The nested VM's program is input as ASCII into the Intcode VM, followed by a final `WALK` or `RUN` command (depending the part), then the Intcode program runs the simulation and outputs either an ASCII rendition of the last few time steps before failure, or a score value on success.

The nested VM can hold up to 15 two-operand instructions. It runs on every time step to decide whether the player shall jump or not. It has six registers, all purely binary: `A` to `D` are read-only and indicate whether there's ground 1 to 4 cells in front of the player, `T` and `J` are free to use. The value of `J` at the end of the program decides whether to jump or not.

There are only three instructions: `AND`, `OR`, and `NOT`, all in 2-operand form, overwriting one of the source registers in case of `AND` and `OR`.

**Part 1** asks for the score produced after a successful `WALK`.

**Part 2** asks the same, but on a different scenario (`RUN`), and with the sensor range extended to **9** cells, introducing registers `E` to `I`.


## Solution Notes

Frustrating dabbling around with boolean logic to match patterns which aren't known beforehand.

* Part 1, Python: 488 bytes, ~150 ms
* Part 2, Python: 540 bytes, ~3.5 s
