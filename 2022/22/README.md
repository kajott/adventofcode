# 2022, Day 22: Monkey Map

The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a _force field_. To pass through the force field, you have to enter a password; doing so involves tracing a specific _path_ on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

## Part 1

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

            ...#
            .#..
            #...
            ....
    ...#.......#
    ........#...
    ..#....#....
    ..........#.
            ...#....
            .....#..
            .#......
            ......#.
    
    10R5L5R10L4R5L5
    

The first half of the monkeys' notes is a _map of the board_. It is comprised of a set of _open tiles_ (on which you can move, drawn `.`) and _solid walls_ (tiles which you cannot enter, drawn `#`).

The second half is a description of _the path you must follow_. It consists of alternating numbers and letters:

*   A _number_ indicates the _number of tiles to move_ in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.
*   A _letter_ indicates whether to turn 90 degrees _clockwise_ (`R`) or _counterclockwise_ (`L`). Turning happens in-place; it does not change your current tile.

So, a path like `10R5` means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing _to the right_ (from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you _wrap around_ to the other side of the board. In other words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at `A` and facing to the right, the tile in front of you is marked `B`; if you are at `C` and facing down, the tile in front of you is marked `D`:

            ...#
            .#..
            #...
            ....
    ...#.D.....#
    ........#...
    B.#....#...A
    .....C....#.
            ...#....
            .....#..
            .#......
            ......#.
    

It is possible for the next tile (after wrapping around) to be a _wall_; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the _last facing you had_ with an arrow on each tile you visit, the full path taken by the above example looks like this:

            >>v#    
            .#v.    
            #.v.    
            ..v.    
    ...#...v..v#    
    >>>v...>#.>>    
    ..#v...#....    
    ...>>>>v..#.    
            ...#....
            .....#..
            .#......
            ......#.
    

To finish providing the password to this strange input device, you need to determine numbers for your final _row_, _column_, and _facing_ as your final position appears from the perspective of the original map. Rows start from `1` at the top and count downward; columns start from `1` at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.) Facing is `0` for right (`>`), `1` for down (`v`), `2` for left (`<`), and `3` for up (`^`). The _final password_ is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is `6`, the final column is `8`, and the final facing is `0`. So, the final password is 1000 \* 6 + 4 \* 8 + 0: _`6032`_.

Follow the path given in the monkeys' notes. _What is the final password?_

Your puzzle answer was `191010`.

## Part 2

As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange _input device_, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large _cube_; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map _does_ have six 50x50 regions on it. If you were to _carefully fold the map_, you should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

            1111
            1111
            1111
            1111
    222233334444
    222233334444
    222233334444
    222233334444
            55556666
            55556666
            55556666
            55556666
    

You still start in the same position and with the same facing as before, but the _wrapping_ rules are different. Now, if you would walk off the board, you instead _proceed around the cube_. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

            ...#
            .#..
            #...
            ....
    ...#.......#
    ........#..A
    ..#....#....
    .D........#.
            ...#..B.
            .....#..
            .#......
            ..C...#.
    

Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:

            ...#
            .#..
         -->#...
            ....
    ...#..E....#
    ........#...
    ..#....#....
    ..........#.
            ...#....
            .....#..
            .#......
            ......#.
    

Using the same method of drawing the _last facing you had_ with an arrow on each tile you visit, the full path taken by the above example now looks like this:

            >>v#    
            .#v.    
            #.v.    
            ..v.    
    ...#..^...v#    
    .>>>>>^.#.>>    
    .^#....#....    
    .^........#.    
            ...#..v.
            .....#v.
            .#v<<<<.
            ..v...#.
    

The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is `5`, the final column is `7`, and the final facing is `3`, so the final password is 1000 \* 5 + 4 \* 7 + 3 = _`5031`_.

Fold the map into a cube, _then_ follow the path given in the monkeys' notes. _What is the final password?_

Your puzzle answer was `55364`.


## Solution Notes

Part 1 is just basic maze traversal code, with the only unusual thing being the odd shape of the maze and the resulting wrapping rules. The star of this show is very clearly part 2, and there are various approaches to take there.

The most obvious one is creating some mapping of the 2D cube net coordinates into the 3D space and then keeping track of the current coordinate in both 2D **and** 3D. I very briefly started doing that, but during 2D->3D map creation, I already noticed that the 3D vector math involved, while not technically very complicated, is still too hard to get exactly right (i.e. without any sign or axis swaps). There must be a better way.

Looking at the 2D net alone, it is clear that at concave corners (i.e. corners where three sides of the net meet), the adjacent edges belong together in 3D space. With that, it's easy to create some kind of "portal" list that maps one of these edges (and the facing direction) to the other, with an appropriately corrected direction. The question is what happens to the edges that are not directly adjacent to a corner. As it turns out, these can be joined with portals as well by simply continuing to "walk along" the edges. Walking starts at concave corners, and at each step, a pair of portals is created (in both directions) and the walk is continued. Walking stops when either side hits another concave corner, or if **both** sides hit a _convex_ (i.e. "outer") corner. This works fine for seven out of eleven possible cube nets; not perfect, but both the example net and the one from the actual input belong into the group that works, so it's good enough for our purposes.

The actual input's net is, in fact, identical for every user who took part in AoC. This means that it's absolutely fine to just hard-code the net, or rather, the resulting portals. My first attempt at this was indeed a bit smaller than the automatic code -- by a whole **two** (in numbers: 2) bytes! The coordinate data for the seven pairs of sides that span the net's circumference was large enough to cancel out almost all of the savings from the removed auto-portal code. It took several rounds of crunching to get the size down to something substantial. The end result of this is an encoding that contains the whole portal list in a single 168-bit number that's encoded in base 36 and decoded with Python's `int` function and a custom radix.

<details><summary><em>(expand this block to see what the data structure looks like)</em></summary>

The 168 bits are comprised of 84 two-bit values; six values for each of the 14 edges of the cube net. The edges, in turn, form seven pairs between which portals are going to be built. The values that define an edge are the following:

| Bits  | Description
|------:|:------
|  1:0  | coarse X start coordinate <br> _(block number; 0-3)_
|    2  | fine   X start coordinate <br> _(0 = left edge, 1 = right edge)_
|  5:4  | coarse Y start coordinate <br> _(block number; 0-3)_
|    6  | fine   Y start coordinate <br> _(0 = top edge, 1 = bottom edge)_
|  9:8  | direction of the edge <br> _(0-3; same encoding as "facing")_
| 11:10 | portal direction <br> _(portal source "facing" value)_

The coordinate encoding might seem a bit strange, but it helps in making the encoding more regular; as said, everything fits into two bits of data, which isn't possible for the "raw" coordinates. There are actually quite a few ways in which data could be saved: The fine coordinates are just 1 bit wide, leaving a gap in the encoding; also, the portal direction is always perpendicular to the edge direction, only the sign isn't clear. In total, it would be possible to save up to 42 bits (leaving 126 bits) if taken to the extreme, but that would require additional decoding logic, which in turn quickly eats up the benefits of a more sophisticated encoding.
</details><br>

* Part 1, Python: 356 bytes, <100 ms
* Part 2, Python (automatic portals): 649 bytes, ~150 ms
* Part 2, Python (hard-coded portals): 557 bytes, <100 ms
