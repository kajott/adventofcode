# 2019, Day 13: Care Package

As you ponder the solitude of space and the ever-increasing three-hour roundtrip for messages between you and Earth, you notice that the Space Mail Indicator Light is blinking. To help keep you sane, the Elves have sent you a care package.

It's a new game for the ship's [arcade cabinet](https://en.wikipedia.org/wiki/Arcade_cabinet)! Unfortunately, the arcade is _all the way_ on the other end of the ship. Surely, it won't be hard to build your own - the care package even comes with schematics.

## Part 1

The arcade cabinet runs [Intcode](9) software like the game the Elves sent (your puzzle input). It has a primitive screen capable of drawing square _tiles_ on a grid. The software draws tiles to the screen with output instructions: every three output instructions specify the `x` position (distance from the left), `y` position (distance from the top), and `tile id`. The `tile id` is interpreted as follows:

*   `0` is an _empty_ tile. No game object appears in this tile.
*   `1` is a _wall_ tile. Walls are indestructible barriers.
*   `2` is a _block_ tile. Blocks can be broken by the ball.
*   `3` is a _horizontal paddle_ tile. The paddle is indestructible.
*   `4` is a _ball_ tile. The ball moves diagonally and bounces off objects.

For example, a sequence of output values like `1,2,3,6,5,4` would draw a _horizontal paddle_ tile (`1` tile from the left and `2` tiles from the top) and a _ball_ tile (`6` tiles from the left and `5` tiles from the top).

Start the game. _How many block tiles are on the screen when the game exits?_

Your puzzle answer was `320`.

## Part 2

The game didn't run because you didn't put in any quarters. Unfortunately, you did not bring any quarters. Memory address `0` represents the number of quarters that have been inserted; set it to `2` to play for free.

The arcade cabinet has a [joystick](https://en.wikipedia.org/wiki/Joystick) that can move left and right. The software reads the position of the joystick with input instructions:

*   If the joystick is in the _neutral position_, provide `0`.
*   If the joystick is _tilted to the left_, provide `-1`.
*   If the joystick is _tilted to the right_, provide `1`.

The arcade cabinet also has a [segment display](https://en.wikipedia.org/wiki/Display_device#Segment_displays) capable of showing a single number that represents the player's current score. When three output instructions specify `X=-1, Y=0`, the third output instruction is not a tile; the value instead specifies the new score to show in the segment display. For example, a sequence of output values like `-1,0,12345` would show `12345` as the player's current score.

Beat the game by breaking all the blocks. _What is your score after the last block is broken?_

Your puzzle answer was `15156`.


## Solution Notes

This is a proper simulation of a Breakout game! The hard (or rather: hard to explain) part like ball physics is in the Intcode program, all the user has to do is provide input. Playing the game as a human is nearly impossible; it's too long and requires *very* precise inputs. So, the actual task is to write a ... well, let's say "AI" for it: Track the ball and paddle positions and have the paddle follow the ball all the time.

For golfing, some shortcuts can be made: Part 1 draws the playfield exactly once, without any overdraw, so counting the drawn block tiles is sufficient. Part 2 doesn't require any kind of display or framebuffer either: The ball and paddle's X positions are simply latched whenever the objects are drawn, and the score is stored if something with a negative X coordinate is output. The Y coordinate isn't used at all.

The golf version expands on this and stores just two dictionaries: The first (`w`) is a map from X coordinates to values; for X >= 0, it doesn't contain anything meaningful (it's the tile ID of the last painted tile in that column), but `w[-1]` contains the current score. The other dictionary (`z`) maps tile IDs to their most recently seen X coordinate, which can then be used to look up the position of the paddle (`z[3]`) and ball (`z[4]`). This dictionary also contains a lot of bogus entries for each score that has been seen in the past (as score updates are just writes into "column -1"); in theory, a score of `3` or `4` could thus disturb the ball/paddle logic. In practice, the score increments per cleared block are around 50 though, so such a situation doesn't occur.

The non-golf implementation contains a console visualization:

    ./intcode.py 13.2-vis

* Part 1, Python: 454 bytes, ~100 ms
* Part 2, Python: 539 bytes, ~3 s
