# [2022, Day 24: Blizzard Basin](https://adventofcode.com/2022/day/24)


## Solution Notes

Moving obstacles may sound scary at first, but it's all smoke and mirrors: The blizzards' positions can be trivially computed at each time step and then they are just normal obstacles, like the walls on the outside. The solution itself is a plain, almost bland BFS; in fact, the (many!) blizzards help in trimming down the search tree a lot -- I don't even reach 1000 open paths for my input.

The only thing that needs consideration is containing the player so they don't take a shortcut via the outside of the maze. An additional, strategically-placed piece of wall above the starting position does the trick, at least for part 1. For part 2, another wall below the exit point is also very much recommended. It's not required though, as the shortcut around the maze is blocked by the wall in front of the start location, but the BFS will visit lots of potential paths in the void outside the maze, making it very slow. The additional 15 bytes for placing the extra wall are rewarded with a ~20x increase in performance.

The golf solutions are not using complex numbers because of all the modulo math involved; this would require lots of "unpacking" (`.real`/`.imag` property access) and "packing" (`x+y*1j`) of numbers, making this approach much more verbose than the traditional 2-tuple method.

The differences between the parts are also relatively small. Part 1 doesn't require multi-goal management and the second wall; the combined code requires a bit more management to only output the times after reaching the first and third goals, but not the second one.

* Part 1, Python: 395 bytes, ~500 ms
* Part 2, Python: 449 bytes, ~1.5 s
* Parts 1+2, Python: 466 bytes, ~1.5 s
