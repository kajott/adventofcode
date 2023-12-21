# 2023, Day 21: Step Counter

You manage to catch the [airship](../07) right as it's dropping someone else off on their all-expenses-paid trip to Desert Island! It even helpfully drops you off near the [gardener](../05) and his massive farm.

"You got the sand flowing again! Great work! Now we just need to wait until we have enough sand to filter the water for Snow Island and we'll have snow again in no time."

While you wait, one of the Elves that works with the gardener heard how good you are at solving problems and would like your help. He needs to get his [steps](https://en.wikipedia.org/wiki/Pedometer) in for the day, and so he'd like to know _which garden plots he can reach with exactly his remaining `64` steps_.

## Part 1

He gives you an up-to-date map (your puzzle input) of his starting position (`S`), garden plots (`.`), and rocks (`#`). For example:

    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#.#....
    .##..S####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    

The Elf starts at the starting position (`S`) which also counts as a garden plot. Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. This would allow him to reach any of the tiles marked `O`:

    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#O#....
    .##.OS####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    

Then, he takes a second step. Since at this point he could be at _either_ tile marked `O`, his second step would allow him to reach any garden plot that is one step north, south, east, or west of _any_ tile that he could have reached after the first step:

    ...........
    .....###.#.
    .###.##..#.
    ..#.#O..#..
    ....#.#....
    .##O.O####.
    .##.O#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    

After two steps, he could be at any of the tiles marked `O` above, including the starting position (either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

    ...........
    .....###.#.
    .###.##..#.
    ..#.#.O.#..
    ...O#O#....
    .##.OS####.
    .##O.#...#.
    ....O..##..
    .##.#.####.
    .##..##.##.
    ...........
    

He will continue like this until his steps for the day have been exhausted. After a total of `6` steps, he could reach any of the garden plots marked `O`:

    ...........
    .....###.#.
    .###.##.O#.
    .O#O#O.O#..
    O.O.#.#.O..
    .##O.O####.
    .##.O#O..#.
    .O.O.O.##..
    .##.#.####.
    .##O.##.##.
    ...........
    

In this example, if the Elf's goal was to get exactly `6` more steps today, he could use them to reach any of _`16`_ garden plots.

However, the Elf _actually needs to get `64` steps today_, and the map he's handed you is much larger than the example map.

Starting from the garden plot marked `S` on your map, _how many garden plots could the Elf reach in exactly `64` steps?_

Your puzzle answer was `3722`.

## Part 2

The Elf seems confused by your answer until he realizes his mistake: he was reading from a list of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.

The _actual_ number of steps he needs to get today is exactly _`26501365`_.

He also points out that the garden plots and rocks are set up so that the map _repeats infinitely_ in every direction.

So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:

    .................................
    .....###.#......###.#......###.#.
    .###.##..#..###.##..#..###.##..#.
    ..#.#...#....#.#...#....#.#...#..
    ....#.#........#.#........#.#....
    .##...####..##...####..##...####.
    .##..#...#..##..#...#..##..#...#.
    .......##.........##.........##..
    .##.#.####..##.#.####..##.#.####.
    .##..##.##..##..##.##..##..##.##.
    .................................
    .................................
    .....###.#......###.#......###.#.
    .###.##..#..###.##..#..###.##..#.
    ..#.#...#....#.#...#....#.#...#..
    ....#.#........#.#........#.#....
    .##...####..##..S####..##...####.
    .##..#...#..##..#...#..##..#...#.
    .......##.........##.........##..
    .##.#.####..##.#.####..##.#.####.
    .##..##.##..##..##.##..##..##.##.
    .................................
    .................................
    .....###.#......###.#......###.#.
    .###.##..#..###.##..#..###.##..#.
    ..#.#...#....#.#...#....#.#...#..
    ....#.#........#.#........#.#....
    .##...####..##...####..##...####.
    .##..#...#..##..#...#..##..#...#.
    .......##.........##.........##..
    .##.#.####..##.#.####..##.#.####.
    .##..##.##..##..##.##..##..##.##.
    .................................
    

This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout; garden plots and rocks repeat as far as you can see. The Elf still starts on the one middle tile marked `S`, though - every other repeated `S` is replaced with a normal garden plot (`.`).

Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:

*   In exactly `6` steps, he can still reach _`16`_ garden plots.
*   In exactly `10` steps, he can reach any of _`50`_ garden plots.
*   In exactly `50` steps, he can reach _`1594`_ garden plots.
*   In exactly `100` steps, he can reach _`6536`_ garden plots.
*   In exactly `500` steps, he can reach _`167004`_ garden plots.
*   In exactly `1000` steps, he can reach _`668697`_ garden plots.
*   In exactly `5000` steps, he can reach _`16733044`_ garden plots.

However, the step count the Elf needs is much larger! Starting from the garden plot marked `S` on your infinite map, _how many garden plots could the Elf reach in exactly `26501365` steps?_

Your puzzle answer was `614864614526014`.

## Solution Notes

Part 1 is almost trivial to solve with out best friend, the set of complex numbers. (For part 2, the switch to tuples had to be made to accomodate the required modulo operations for the obstacle coordinates.)

Part 2 is clearly another "find the cycle and extrapolate" kind of problem. In this case, the number of reachable spots for each time step modulo the maze size follows a quadratic progression. (It may not be immediately obvious why, but it actually makes sense: It's quadratic because it expands in area, and the period size is equal to the maze size, because what else could it be that makes the problem periodic?) So run the simulation, note the results for each time step that's 26501365 modulo the maze size until three samples have been found, and extrapolate the quadratic function. That's what my initial approach did.

The problem with this first attempt was runtime. While ~18 seconds isn't totally off the charts, it's still unwieldy. (I already sacrificed a whopping 3 bytes in order to avoid another 2x slowdown!) There needs to be something else that can be optimized, and of course there is! Not only is the problem periodic modulo the maze size, there's also a certain periodicity between odd and even time steps: At t+1, the reachable spots are going to be mostly the same as at t-1, except for a few extra spots on the periphery. This means that it's sufficient to simulate the "active edge" and ignore all interior spots, causing the runtime to drop dramatically, because instead of O(t^2) positions, only O(t) positions need to be evaluated. This optimization costs a few bytes (roughly 10% of the total size), but it's easily worth it.

* Part 1, Python: 191 bytes, <100 ms
* Part 2, Python (full simulation): 329 bytes, ~20 s
* Part 2, Python (edge only): 358 bytes, ~600 ms
