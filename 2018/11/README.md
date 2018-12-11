# 2018, Day 11: Chronal Charge

You watch the Elves and their sleigh fade into the distance as they head toward the North Pole.

Actually, you're the one fading. The falling sensation returns.

## Part 1

The low fuel warning light is illuminated on your wrist-mounted device. Tapping it once causes it to project a hologram of the situation: a _300x300_ grid of fuel cells and their current power levels, some negative. You're not sure what negative power means in the context of time travel, but it can't be good.

Each fuel cell has a coordinate ranging _from 1 to 300_ in both the X (horizontal) and Y (vertical) direction. In `X,Y` notation, the top-left cell is `1,1`, and the top-right cell is `300,1`.

The interface lets you select _any 3x3 square_ of fuel cells. To increase your chances of getting to your destination, you decide to choose the 3x3 square with the _largest total power_.

The power level in a given fuel cell can be found through the following process:

*   Find the fuel cell's _rack ID_, which is its _X coordinate plus 10_.
*   Begin with a power level of the _rack ID_ times the _Y coordinate_.
*   Increase the power level by the value of the _grid serial number_ (your puzzle input).
*   Set the power level to itself multiplied by the _rack ID_.
*   Keep only the _hundreds digit_ of the power level (so `12`_`3`_`45` becomes `3`; numbers with no hundreds digit become `0`).
*   _Subtract 5_ from the power level.

For example, to find the power level of the fuel cell at `3,5` in a grid with serial number `8`:

*   The rack ID is `3 + 10 =` _`13`_.
*   The power level starts at `13 * 5 =` _`65`_.
*   Adding the serial number produces `65 + 8 =` _`73`_.
*   Multiplying by the rack ID produces `73 * 13 =` _`949`_.
*   The hundreds digit of _`9`_`49` is _`9`_.
*   Subtracting 5 produces `9 - 5 =` _`4`_.

So, the power level of this fuel cell is `_4_`.

Here are some more example power levels:

*   Fuel cell at  `122,79`, grid serial number `57`: power level `-5`.
*   Fuel cell at `217,196`, grid serial number `39`: power level  `0`.
*   Fuel cell at `101,153`, grid serial number `71`: power level  `4`.

Your goal is to find the 3x3 square which has the largest total power. The square must be entirely within the 300x300 grid. Identify this square using the `X,Y` coordinate of its _top-left fuel cell_. For example:

For grid serial number `18`, the largest total 3x3 square has a top-left corner of _`33,45`_ (with a total power of `29`); these fuel cells appear in the middle of this 5x5 region:

    -2  -4   4   4   4
    -4   4   4   4  -5
     4   3   3   4  -4
     1   1   2   4  -3
    -1   0   2  -5  -2
    

For grid serial number `42`, the largest 3x3 square's top-left is _`21,61`_ (with a total power of `30`); they are in the middle of this region:

    -3   4   2   2   2
    -4   4   3   3   4
    -5   3   3   4  -4
     4   3   3   4  -3
     3   3   3  -5  -1
    

_What is the `X,Y` coordinate of the top-left fuel cell of the 3x3 square with the largest total power?_

Your puzzle input was `7989`.

Your puzzle answer was `19,17`.

## Part 2

You discover a dial on the side of the device; it seems to let you select a square of _any size_, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the _square of any size with the largest total power_. Identify this square by including its size as a third parameter after the top-left coordinate: a 9x9 square with a top-left corner of `3,5` is identified as `3,5,9`.

For example:

*   For grid serial number `18`, the largest total square (with a total power of `113`) is 16x16 and has a top-left corner of `90,269`, so its identifier is _`90,269,16`_.
*   For grid serial number `42`, the largest total square (with a total power of `119`) is 12x12 and has a top-left corner of `232,251`, so its identifier is _`232,251,12`_.

_What is the `X,Y,size` identifier of the square with the largest total power?_

Your puzzle input was still `7989`.

Your puzzle answer was `233,288,12`.


## Solution Notes

This is one of the "hah, your naive solution won't scale for part 2" puzzles. Indeed, my first approach runs almost 10 minutes in total, though the correct result is already produced after little more than 2 seconds -- but what if a there's a better result at a larger summation size?. (It's unlikely, as the overall matrix has a small negative bias, favoring smaller summations, but you can't be sure.)

The first optimization step is to pre-compute a matrix with NxN sub-square sums for each size and then finding the maximum. This already reduced the computation time to 3% of the initial approach for me. But the pre-computation itself was still implemented in a naive manner, so I optimized this again and got down to less than five seconds for the full solution in Python.

In C, I got down to less than 100 milliseconds, *including* compilation (40 ms without). This time, compiler optimization was a net win, i.e. it makes the code so much faster (~3x) that the longer compile times are more than compensated.

* Part 1, Python: 216 bytes, ~100 ms
* Part 2, Python (naive): 281 bytes, ~10 minutes
* Part 2, Python (pre-summed matrix): 335 bytes, ~15 s
* Part 2, Python (optimized pre-summed matrix): 385 bytes, ~3.5 s
* Part 2, C: 438 bytes, <100 ms
