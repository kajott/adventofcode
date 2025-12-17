# [2019, Day 13: Care Package](https://adventofcode.com/2019/day/13)


## Solution Notes

This is a proper simulation of a Breakout game! The hard (or rather: hard to explain in prose) problems like ball/paddle/brick physics are encoded in the Intcode program, and all the user has to do is provide input. Playing the game as a human is nearly impossible; it's too long and requires *very* precisely timed inputs. So, the actual task is to write a ... well, let's say "AI" for it: Track the ball and paddle positions and have the paddle follow the ball all the time.

For golfing, some shortcuts can be made: Part 1 draws the playfield exactly once, without any overdraw, so counting the drawn block tiles is sufficient. Part 2 doesn't require any kind of display or framebuffer either: The ball and paddle's X positions are simply latched whenever the objects are drawn, and the score is stored if something with a negative X coordinate is output. The Y coordinate isn't used at all.

The golf version expands on this and stores just two dictionaries: The first (`w`) is a map from X coordinates to values; for X >= 0, it doesn't contain anything meaningful (it's the tile ID of the last painted tile in that column), but `w[-1]` contains the current score. The other dictionary (`z`) maps tile IDs to their most recently seen X coordinate, which can then be used to look up the position of the paddle (`z[3]`) and ball (`z[4]`). This dictionary also contains a lot of bogus entries for each score that has been seen in the past (as score updates are just writes of arbitrary large values); in theory, a score of `3` or `4` could thus disturb the ball/paddle logic. In practice, the score increments per cleared block are around 50 though, so such a situation doesn't occur.

The non-golf implementation contains a console visualization:

    ./intcode.py 13.2-vis

* Part 1, Python: 432 bytes, ~100 ms
* Part 2, Python: 517 bytes, ~3 s
