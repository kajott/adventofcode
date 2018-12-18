# 2018, Day 18: Settlers of The North Pole

On the outskirts of the North Pole base construction project, many Elves are collecting lumber.

## Part 1

The lumber collection area is 50 acres by 50 acres; each acre can be either _open ground_ (`.`), _trees_ (`|`), or a _lumberyard_ (`#`). You take a scan of the area (your puzzle input).

Strange magic is at work here: each minute, the landscape looks entirely different. In exactly _one minute_, an open acre can fill with trees, a wooded acre can be converted to a lumberyard, or a lumberyard can be cleared to open ground (the lumber having been sent to other projects).

The change to each acre is based entirely on _the contents of that acre_ as well as _the number of open, wooded, or lumberyard acres adjacent to it_ at the start of each minute. Here, "adjacent" means any of the eight acres surrounding that acre. (Acres on the edges of the lumber collection area might have fewer than eight adjacent acres; the missing acres aren't counted.)

In particular:

*   An _open_ acre will become filled with _trees_ if _three or more_ adjacent acres contained trees. Otherwise, nothing happens.
*   An acre filled with _trees_ will become a _lumberyard_ if _three or more_ adjacent acres were lumberyards. Otherwise, nothing happens.
*   An acre containing a _lumberyard_ will remain a _lumberyard_ if it was adjacent to _at least one other lumberyard and at least one acre containing trees_. Otherwise, it becomes _open_.

These changes happen across all acres _simultaneously_, each of them using the state of all acres at the beginning of the minute and changing to their new form by the end of that same minute. Changes that happen during the minute don't affect each other.

For example, suppose the lumber collection area is instead only 10 by 10 acres with this initial configuration:

    Initial state:
    .#.#...|#.
    .....#|##|
    .|..|...#.
    ..|#.....#
    #.#|||#|#|
    ...#.||...
    .|....|...
    ||...#|.#|
    |.||||..|.
    ...#.|..|.
    
    After 1 minute:
    .......##.
    ......|###
    .|..|...#.
    ..|#||...#
    ..##||.|#|
    ...#||||..
    ||...|||..
    |||||.||.|
    ||||||||||
    ....||..|.
    
    After 2 minutes:
    .......#..
    ......|#..
    .|.|||....
    ..##|||..#
    ..###|||#|
    ...#|||||.
    |||||||||.
    ||||||||||
    ||||||||||
    .|||||||||
    
    After 3 minutes:
    .......#..
    ....|||#..
    .|.||||...
    ..###|||.#
    ...##|||#|
    .||##|||||
    ||||||||||
    ||||||||||
    ||||||||||
    ||||||||||
    
    After 4 minutes:
    .....|.#..
    ...||||#..
    .|.#||||..
    ..###||||#
    ...###||#|
    |||##|||||
    ||||||||||
    ||||||||||
    ||||||||||
    ||||||||||
    
    After 5 minutes:
    ....|||#..
    ...||||#..
    .|.##||||.
    ..####|||#
    .|.###||#|
    |||###||||
    ||||||||||
    ||||||||||
    ||||||||||
    ||||||||||
    
    After 6 minutes:
    ...||||#..
    ...||||#..
    .|.###|||.
    ..#.##|||#
    |||#.##|#|
    |||###||||
    ||||#|||||
    ||||||||||
    ||||||||||
    ||||||||||
    
    After 7 minutes:
    ...||||#..
    ..||#|##..
    .|.####||.
    ||#..##||#
    ||##.##|#|
    |||####|||
    |||###||||
    ||||||||||
    ||||||||||
    ||||||||||
    
    After 8 minutes:
    ..||||##..
    ..|#####..
    |||#####|.
    ||#...##|#
    ||##..###|
    ||##.###||
    |||####|||
    ||||#|||||
    ||||||||||
    ||||||||||
    
    After 9 minutes:
    ..||###...
    .||#####..
    ||##...##.
    ||#....###
    |##....##|
    ||##..###|
    ||######||
    |||###||||
    ||||||||||
    ||||||||||
    
    After 10 minutes:
    .||##.....
    ||###.....
    ||##......
    |##.....##
    |##.....##
    |##....##|
    ||##.####|
    ||#####|||
    ||||#|||||
    ||||||||||
    

After 10 minutes, there are `37` wooded acres and `31` lumberyards. Multiplying the number of wooded acres by the number of lumberyards gives the total _resource value_ after ten minutes: `37 * 31 =` _`1147`_.

_What will the total resource value of the lumber collection area be after 10 minutes?_

Your puzzle answer was `598416`.

## Part 2

This important natural resource will need to last for at least thousands of years. Are the Elves collecting this lumber sustainably?

_What will the total resource value of the lumber collection area be after 1000000000 minutes?_

Your puzzle answer was `196310`.


## Solution Notes

This puzzle is very similar to 2018 day 12: A straightforward cellular automaton simulation (this time in 2D) with an absurdly large iteration count. Again, the task in part 2 is to recognize a pattern in the output over time; specifically, that there is a cycle in which the whole world's state starts to oscillate after a few hundred iterations.

* Part 1, Python: 465 bytes, <100 ms
* Part 2, Python: 570 bytes, ~2.5 s
