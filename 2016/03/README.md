# 2016, Day 3: Squares With Three Sides

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

## Part 1

The design document gives the side lengths of each triangle it describes, but... `5 10 25`? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because `5 + 10` is not larger than `25`.

In your puzzle input, _how many_ of the listed triangles are _possible_?

Your puzzle answer was `917`.

## Part 2

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three _vertically_. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

    101 301 501
    102 302 502
    103 303 503
    201 401 601
    202 402 602
    203 403 603
    

In your puzzle input, and instead reading by columns, _how many_ of the listed triangles are _possible_?

Your puzzle answer was `1649`.


## Solution Notes

Part 1 is a nice oneliner that almost fits onto a normal 80-column terminal screen, and part 2 is only marginally more complex, as it's just an additional transposition.

* Part 1, Python: 84 bytes, <100 ms
* Part 2, Python: 143 bytes, <100 ms
