# 2021, Day 3: Binary Diagnostic


## Solution Notes

For the first part, the input can simply be read as a 2D array of bits, transposed, and a majority vote can be computed. The "epsilon rate" can be computed from the "gamma rate" by flipping all the bits.

The second part can be done in a similar way, but I opted for parsing the numbers and using them as such. The code itself is then just a boring by-the-letter implementation of the task description, with some bit fiddling stuff for the majority vote and selection process.

* Part 1, Python: 120 bytes, <100 ms
* Part 2, Python: 181 bytes, <100 ms
