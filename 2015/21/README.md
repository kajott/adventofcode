# [2015, Day 21: RPG Simulator 20XX](https://adventofcode.com/2015/day/21)


## Solution Notes

This is one of these puzzles where following the description to the letter is very important. I spent a considerable amount of time debugging part 2 until I noticed that I didn't allow the player to have no base armor ...

A full simulation of the battles isn't necessary, as each attack deals a constant amount of damage. It all boils down to a simple division and a comparison.

The real fun in code golf for this puzzle is encoding the shop inventory in a compact way.

* Part 1, Python: 335 bytes, <100 ms
* Part 2, Python: 334 bytes, <100 ms
