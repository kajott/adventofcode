# [2025, Day 6: Trash Compactor](https://adventofcode.com/2025/day/6)

The input consists of (typically) four lines of (typically) 1000 numbers of 1 to 4 digits with whitespace inbetween, plus an additional line with either plus signs (`+`) or stars (`*`). The numbers and signs are aligned to form full columns.

**Part 1** asks for the results of the additions or multiplication of each **column**.

**Part 2** changes the interpretation of the numbers themselves to be column-oriented, i.e. each operand to the addition or multiplication is itself spread out over the four lines.


## Solution Notes

Two very simple tasks that just need to executed exactly as written down. Part 2 is a bit special in that any attempt to mess with the whitespace in the input is going to produce incorrect results; in particular, the parser of part 1 can't be reused.

It's _extremely_ tempting to use the evil `eval()` to compute the results; in fact, that's by far the simplest and most compact approach. Doing it the "proper" and safe way means converting the strings to integers and dispatching to `sum` or `math.prod` depending on the operation ... bleh!

* Part 1, Python (using `eval`): 89 bytes, <100 ms
* Part 1, Python (safe): 131 bytes, <100 ms
* Part 2, Python (using `eval`): 155 bytes, <100 ms
* Part 2, Python (safe): 187 bytes, <100 ms
