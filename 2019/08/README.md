# [2019, Day 8: Space Image Format](https://adventofcode.com/2019/day/8)

The input consists of a (typically) 15000-digit ternary string. This is to be interpreted as an image with (typically) 100 layers of 25x6 pixels. Each pixel can be either black (`0`), white (`1`) or transparent (`2`).

**Part 1** asks to find the layer with the fewest `0` digits.

**Part 2** asks to merge the layers, with proper handling of transparent pixels, and read the letters that appear in the resulting image.


## Solution Notes

A nice and simple puzzle, nothing much else to write here.

* Part 1, Python: 166 bytes, <100 ms
* Part 2, Python: 200 bytes, <100 ms
