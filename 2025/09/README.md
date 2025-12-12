# 2025, Day 9: Movie Theater

You slide down the [firepole](https://en.wikipedia.org/wiki/Fireman%27s_pole) in the corner of the playground and land in the North Pole base movie theater!

## Part 1

The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are _red_; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

For example:

    7,1
    11,1
    11,7
    9,7
    9,5
    2,5
    2,3
    7,3
    

Showing red tiles as `#` and other tiles as `.`, the above arrangement of red tiles would look like this:

    ..............
    .......#...#..
    ..............
    ..#....#......
    ..............
    ..#......#....
    ..............
    .........#.#..
    ..............
    

You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

For example, you could make a rectangle (shown as `O`) with an area of `24` between `2,5` and `9,7`:

    ..............
    .......#...#..
    ..............
    ..#....#......
    ..............
    ..OOOOOOOO....
    ..OOOOOOOO....
    ..OOOOOOOO.#..
    ..............
    

Or, you could make a rectangle with area `35` between `7,1` and `11,7`:

    ..............
    .......OOOOO..
    .......OOOOO..
    ..#....OOOOO..
    .......OOOOO..
    ..#....OOOOO..
    .......OOOOO..
    .......OOOOO..
    ..............
    

You could even make a thin rectangle with an area of only `6` between `7,3` and `2,3`:

    ..............
    .......#...#..
    ..............
    ..OOOOOO......
    ..............
    ..#......#....
    ..............
    .........#.#..
    ..............
    

Ultimately, the largest rectangle you can make in this example has area _`50`_. One way to do this is between `2,5` and `11,1`:

    ..............
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..............
    .........#.#..
    ..............
    

Using two red tiles as opposite corners, _what is the largest area of any rectangle you can make?_

Your puzzle answer was `4744899849`.

## Part 2

The Elves just remembered: they can only switch out tiles that are _red_ or _green_. So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it by a straight line of _green tiles_. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

Using the same example as before, the tiles marked `X` would be green:

    ..............
    .......#XXX#..
    .......X...X..
    ..#XXXX#...X..
    ..X........X..
    ..#XXXXXX#.X..
    .........X.X..
    .........#X#..
    ..............
    

In addition, all of the tiles _inside_ this loop of red and green tiles are _also_ green. So, in this example, these are the green tiles:

    ..............
    .......#XXX#..
    .......XXXXX..
    ..#XXXX#XXXX..
    ..XXXXXXXXXX..
    ..#XXXXXX#XX..
    .........XXX..
    .........#X#..
    ..............
    

The remaining tiles are never red nor green.

The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

For example, you could make a rectangle out of red and green tiles with an area of `15` between `7,3` and `11,1`:

    ..............
    .......OOOOO..
    .......OOOOO..
    ..#XXXXOOOOO..
    ..XXXXXXXXXX..
    ..#XXXXXX#XX..
    .........XXX..
    .........#X#..
    ..............
    

Or, you could make a thin rectangle with an area of `3` between `9,7` and `9,5`:

    ..............
    .......#XXX#..
    .......XXXXX..
    ..#XXXX#XXXX..
    ..XXXXXXXXXX..
    ..#XXXXXXOXX..
    .........OXX..
    .........OX#..
    ..............
    

The largest rectangle you can make in this example using only red and green tiles has area _`24`_. One way to do this is between `9,5` and `2,3`:

    ..............
    .......#XXX#..
    .......XXXXX..
    ..OOOOOOOOXX..
    ..OOOOOOOOXX..
    ..OOOOOOOOXX..
    .........XXX..
    .........#X#..
    ..............
    

Using two red tiles as opposite corners, _what is the largest area of any rectangle you can make using only red and green tiles?_

Your puzzle answer was `1540192500`.


## Solution Notes

Part 1 is nothing of note, part 2 is really where the meat is. And what a hunk of meat indeed! My first approach was to actually paint the path into a grid (or rather a set of complex numbers), use a flood fill to fill the interior (with multiple different seed points, trying them until one does *not* spill outside of the map), and then check every possible box if it's completely filled. Coordinate compression (a technique I've [used before](../../2013/18)) turns the large values from the actual input into something more manageable. However, that's a lot of steps and rather ugly code, and it's sloooow - over 1 minute on a really fast machine. I completely discarded this approach, because it's also very much unsuitable for code golf.

Instead, a much more elegant approach is now used that doesn't even start to rasterize the path in any way, shape or form. It's basically the same "find maximum area" loop as in part 1, but with an extra condition: a box is only eligible if it doesn't intersect with the polygon. To check that, it is sufficient to check whether any horizontal or vertical line that make up the polygon are intersecting with the perimeter of the box. It's not required to overthink things: Establishing the boundary conditions can be extremely prone to off-by-one errors, particularily in cases where two parallel lines have a distance of only 1 unit, and also, it would be required to check if a box is inside the polygon at all, etc. ... But none of this matters, as the input is relatively benign. The only trap, if you want to call it that way, is a thin wide strip of negative space right in the middle of the (circular, by the way) figure.

The non-golf version runs in 2-3 seconds, but for some reason, CPython 3.13 (which is the version I've been using at the time of writing) is unreasonably slow when running the golf version, even though it's doing basically the same things. I actually spent 16 not strictly necessary bytes to bring runtime down from almost a minute to what I have now. (Remove the `if k<1:break` line and see for yourself.) I've yet to find an explanation for this performance regression, but in the meantime, I take solace in the fact that at least PyPy runs everything in less than a second.

* Part 1, Python: 135 bytes, <100 ms
* Part 2, Python: 343 bytes, ~25 s
