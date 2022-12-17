# 2022, Day 17: Pyroclastic Flow

Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

## Part 1

The five types of rocks have the following peculiar shapes, where `#` is rock and `.` is empty space:

    ####
    
    .#.
    ###
    .#.
    
    ..#
    ..#
    ###
    
    #
    #
    #
    #
    
    ##
    ##
    

The rocks fall in the order shown above: first the `-` shape, then the `+` shape, and so on. Once the end of the list is reached, the same order repeats: the `-` shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

    >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
    

In jet patterns, `<` means a push to the left, while `>` means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

The tall, vertical chamber is exactly _seven units wide_. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

After a rock appears, it alternates between _being pushed by a jet of hot gas_ one unit (in the direction indicated by the next symbol in the jet pattern) and then _falling one unit down_. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a _downward_ movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

Drawing falling rocks with `@` and stopped rocks with `#`, the jet pattern in the example above manifests as follows:

    The first rock begins falling:
    |..@@@@.|
    |.......|
    |.......|
    |.......|
    +-------+
    
    Jet of gas pushes rock right:
    |...@@@@|
    |.......|
    |.......|
    |.......|
    +-------+
    
    Rock falls 1 unit:
    |...@@@@|
    |.......|
    |.......|
    +-------+
    
    Jet of gas pushes rock right, but nothing happens:
    |...@@@@|
    |.......|
    |.......|
    +-------+
    
    Rock falls 1 unit:
    |...@@@@|
    |.......|
    +-------+
    
    Jet of gas pushes rock right, but nothing happens:
    |...@@@@|
    |.......|
    +-------+
    
    Rock falls 1 unit:
    |...@@@@|
    +-------+
    
    Jet of gas pushes rock left:
    |..@@@@.|
    +-------+
    
    Rock falls 1 unit, causing it to come to rest:
    |..####.|
    +-------+
    
    A new rock begins falling:
    |...@...|
    |..@@@..|
    |...@...|
    |.......|
    |.......|
    |.......|
    |..####.|
    +-------+
    
    Jet of gas pushes rock left:
    |..@....|
    |.@@@...|
    |..@....|
    |.......|
    |.......|
    |.......|
    |..####.|
    +-------+
    
    Rock falls 1 unit:
    |..@....|
    |.@@@...|
    |..@....|
    |.......|
    |.......|
    |..####.|
    +-------+
    
    Jet of gas pushes rock right:
    |...@...|
    |..@@@..|
    |...@...|
    |.......|
    |.......|
    |..####.|
    +-------+
    
    Rock falls 1 unit:
    |...@...|
    |..@@@..|
    |...@...|
    |.......|
    |..####.|
    +-------+
    
    Jet of gas pushes rock left:
    |..@....|
    |.@@@...|
    |..@....|
    |.......|
    |..####.|
    +-------+
    
    Rock falls 1 unit:
    |..@....|
    |.@@@...|
    |..@....|
    |..####.|
    +-------+
    
    Jet of gas pushes rock right:
    |...@...|
    |..@@@..|
    |...@...|
    |..####.|
    +-------+
    
    Rock falls 1 unit, causing it to come to rest:
    |...#...|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    A new rock begins falling:
    |....@..|
    |....@..|
    |..@@@..|
    |.......|
    |.......|
    |.......|
    |...#...|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    

The moment each of the next few rocks begins falling, you would see this:

    |..@....|
    |..@....|
    |..@....|
    |..@....|
    |.......|
    |.......|
    |.......|
    |..#....|
    |..#....|
    |####...|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    |..@@...|
    |..@@...|
    |.......|
    |.......|
    |.......|
    |....#..|
    |..#.#..|
    |..#.#..|
    |#####..|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    |..@@@@.|
    |.......|
    |.......|
    |.......|
    |....##.|
    |....##.|
    |....#..|
    |..#.#..|
    |..#.#..|
    |#####..|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    |...@...|
    |..@@@..|
    |...@...|
    |.......|
    |.......|
    |.......|
    |.####..|
    |....##.|
    |....##.|
    |....#..|
    |..#.#..|
    |..#.#..|
    |#####..|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    |....@..|
    |....@..|
    |..@@@..|
    |.......|
    |.......|
    |.......|
    |..#....|
    |.###...|
    |..#....|
    |.####..|
    |....##.|
    |....##.|
    |....#..|
    |..#.#..|
    |..#.#..|
    |#####..|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    |..@....|
    |..@....|
    |..@....|
    |..@....|
    |.......|
    |.......|
    |.......|
    |.....#.|
    |.....#.|
    |..####.|
    |.###...|
    |..#....|
    |.####..|
    |....##.|
    |....##.|
    |....#..|
    |..#.#..|
    |..#.#..|
    |#####..|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    |..@@...|
    |..@@...|
    |.......|
    |.......|
    |.......|
    |....#..|
    |....#..|
    |....##.|
    |....##.|
    |..####.|
    |.###...|
    |..#....|
    |.####..|
    |....##.|
    |....##.|
    |....#..|
    |..#.#..|
    |..#.#..|
    |#####..|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    
    |..@@@@.|
    |.......|
    |.......|
    |.......|
    |....#..|
    |....#..|
    |....##.|
    |##..##.|
    |######.|
    |.###...|
    |..#....|
    |.####..|
    |....##.|
    |....##.|
    |....#..|
    |..#.#..|
    |..#.#..|
    |#####..|
    |..###..|
    |...#...|
    |..####.|
    +-------+
    

To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be _`3068`_ units tall.

_How many units tall will the tower of rocks be after 2022 rocks have stopped falling?_

Your puzzle answer was `3141`.

## Part 2

The elephants are not impressed by your simulation. They demand to know how tall the tower will be after _`1000000000000`_ rocks have stopped! Only then will they feel confident enough to proceed through the cave.

In the example above, the tower would be _`1514285714288`_ units tall!

_How tall will the tower be after `1000000000000` rocks have stopped?_

Your puzzle answer was `1561739130391`.

## Solution Notes

Part 1 is a straightforward simulation of an almost-but-not-quite Tetris game. The most interesting question in my mind, while writing the initial non-golf version for the contest, is what part 2 is going to be. More tiles? Rotating tiles? Maybe wider playfields? It's because of the latter question that I initially used sets of `(x,y)` tuples to represent the chamber state; if I had known that part 2 is using the same 7-wide playfield, I'd have used bitfields instead, and consequently, this is what I did for the golf version. It's just soooo much more convenient.

What part 2 did ultimately turn out to be, though, is a rather nasty (if [predictable](../../2018/12)) surprise. So, it's all about finding some periodic pattern and applying it appropriately. The shortest period that can possibly emerge is certainly the length of the input (which seems to be always 10091, and hence prime) times the number of different bricks, i.e. 5. But what should this period be applied to? That's really a head-scrather, because it *not* apply to the number of blocks, for example.

What I did (and what seems to work for multiple people's inputs), is the following:
- Let the simulation run for as many blocks (_not_ time steps, curiously!) until the input has been repeated five times. (This may happen in the middle of a block simulation, but it doesn't matter.) Note the number of blocks and stack height.
- Continue the simulation until the input has been repeated another five times. The _increase_ in block count and stack height during this phase will stay the same for every subsequent run of five input cycles, so it can conveniently be used to make a projection of how high the stack will be until a bit before the 1 billion (or trillion, YMMV) block mark.
- Run the simulation for the remaining number of blocks, and add the _increase_ in stack height to the projection to get the final result.

I'm not 100% if that is the best way to do it, but it works fine for me, it's convenient enough and has good performance.

* Part 1, Python: 366 bytes, <100 ms
* Part 2, Python: 468 bytes, ~350 ms
