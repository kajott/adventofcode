# 2022, Day 24: Blizzard Basin

With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.

Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.

At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.

As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small _blizzards_ of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.

## Part 1

Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:

    #.#####
    #.....#
    #>....#
    #.....#
    #...v.#
    #.....#
    #####.#
    

The walls of the valley are drawn as `#`; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as `.`. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (`^`), down (`v`), left (`<`), or right (`>`).

The above map includes two blizzards, one moving right (`>`) and one moving down (`v`). In one minute, each blizzard moves one position in the direction it is pointing:

    #.#####
    #.....#
    #.>...#
    #.....#
    #.....#
    #...v.#
    #####.#
    

Due to conservation of blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:

    #.#####
    #...v.#
    #..>..#
    #.....#
    #.....#
    #.....#
    #####.#
    

Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked `2`:

    #.#####
    #.....#
    #...2.#
    #.....#
    #.....#
    #.....#
    #####.#
    

After another minute, the situation resolves itself, giving each blizzard back its personal space:

    #.#####
    #.....#
    #....>#
    #...v.#
    #.....#
    #.....#
    #####.#
    

Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:

    #.#####
    #.....#
    #>....#
    #.....#
    #...v.#
    #.....#
    #####.#
    

This process repeats at least as long as you are observing it, but probably forever.

Here is a more complex example:

    #.######
    #>>.<^<#
    #.<..<<#
    #>v.><>#
    #<^v^^>#
    ######.#
    

Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can _move_ up, down, left, or right, or you can _wait_ in place. You and the blizzards act _simultaneously_, and you cannot share a position with a blizzard.

In the above example, the fastest way to reach your goal requires _`18`_ steps. Drawing the position of the expedition as `E`, one way to achieve this is:

    Initial state:
    #E######
    #>>.<^<#
    #.<..<<#
    #>v.><>#
    #<^v^^>#
    ######.#
    
    Minute 1, move down:
    #.######
    #E>3.<.#
    #<..<<.#
    #>2.22.#
    #>v..^<#
    ######.#
    
    Minute 2, move down:
    #.######
    #.2>2..#
    #E^22^<#
    #.>2.^>#
    #.>..<.#
    ######.#
    
    Minute 3, wait:
    #.######
    #<^<22.#
    #E2<.2.#
    #><2>..#
    #..><..#
    ######.#
    
    Minute 4, move up:
    #.######
    #E<..22#
    #<<.<..#
    #<2.>>.#
    #.^22^.#
    ######.#
    
    Minute 5, move right:
    #.######
    #2Ev.<>#
    #<.<..<#
    #.^>^22#
    #.2..2.#
    ######.#
    
    Minute 6, move right:
    #.######
    #>2E<.<#
    #.2v^2<#
    #>..>2>#
    #<....>#
    ######.#
    
    Minute 7, move down:
    #.######
    #.22^2.#
    #<vE<2.#
    #>>v<>.#
    #>....<#
    ######.#
    
    Minute 8, move left:
    #.######
    #.<>2^.#
    #.E<<.<#
    #.22..>#
    #.2v^2.#
    ######.#
    
    Minute 9, move up:
    #.######
    #<E2>>.#
    #.<<.<.#
    #>2>2^.#
    #.v><^.#
    ######.#
    
    Minute 10, move right:
    #.######
    #.2E.>2#
    #<2v2^.#
    #<>.>2.#
    #..<>..#
    ######.#
    
    Minute 11, wait:
    #.######
    #2^E^2>#
    #<v<.^<#
    #..2.>2#
    #.<..>.#
    ######.#
    
    Minute 12, move down:
    #.######
    #>>.<^<#
    #.<E.<<#
    #>v.><>#
    #<^v^^>#
    ######.#
    
    Minute 13, move down:
    #.######
    #.>3.<.#
    #<..<<.#
    #>2E22.#
    #>v..^<#
    ######.#
    
    Minute 14, move right:
    #.######
    #.2>2..#
    #.^22^<#
    #.>2E^>#
    #.>..<.#
    ######.#
    
    Minute 15, move right:
    #.######
    #<^<22.#
    #.2<.2.#
    #><2>E.#
    #..><..#
    ######.#
    
    Minute 16, move right:
    #.######
    #.<..22#
    #<<.<..#
    #<2.>>E#
    #.^22^.#
    ######.#
    
    Minute 17, move down:
    #.######
    #2.v.<>#
    #<.<..<#
    #.^>^22#
    #.2..2E#
    ######.#
    
    Minute 18, move down:
    #.######
    #>2.<.<#
    #.2v^2<#
    #>..>2>#
    #<....>#
    ######E#
    

_What is the fewest number of minutes required to avoid the blizzards and reach the goal?_

Your puzzle answer was `295`.

## Part 2

As the expedition reaches the far side of the valley, one of the Elves looks especially dismayed:

He _forgot his snacks_ at the entrance to the valley!

Since you're so good at dodging blizzards, the Elves humbly request that you go back for his snacks. From the same initial conditions, how quickly can you make it from the start to the goal, then back to the start, then back to the goal?

In the above example, the first trip to the goal takes `18` minutes, the trip back to the start takes `23` minutes, and the trip back to the goal again takes `13` minutes, for a total time of _`54`_ minutes.

_What is the fewest number of minutes required to reach the goal, go back to the start, then reach the goal again?_

Your puzzle answer was `851`.


## Solution Notes

Moving obstacles may sound scary at first, but it's all smoke and mirrors: The blizzards' positions can be trivially computed at each time step and then they are just normal obstacles, like the walls on the outside. The solution itself is a plain, almost bland BFS; in fact, the (many!) blizzards help in trimming down the search tree a lot -- I don't even reach 1000 open paths for my input.

The only thing that needs consideration is containing the player so they don't take a shortcut via the outside of the maze. An additional, strategically-placed piece of wall above the starting position does the trick, at least for part 1. For part 2, another wall below the exit point is also very much recommended. It's not required though, as the shortcut around the maze is blocked by the wall in front of the start location, but the BFS will visit lots of potential paths in the void outside the maze, making it very slow. The additional 15 bytes for placing the extra wall are rewarded with a ~20x increase in performance.

The golf solutions are not using complex numbers because of all the modulo math involved; this would require lots of "unpacking" (`.real`/`.imag` property access) and "packing" (`x+y*1j`) of numbers, making this approach much more verbose than the traditional 2-tuple method.

The differences between the parts are also relatively small. Part 1 doesn't require multi-goal management and the second wall; the combined code requires a bit more management to only output the times after reaching the first and third goals, but not the second one.

* Part 1, Python: 395 bytes, ~500 ms
* Part 2, Python: 449 bytes, ~1.5 s
* Parts 1+2, Python: 466 bytes, ~1.5 s
