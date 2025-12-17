# 2021, Day 2: Dive!


## Solution Notes

As with every task that has to do with 2D coordinates, complex numbers seem to be a good pick for part 1 here, but in terms of code golf, these actually turn out to be sub-optimal, because the final multiplication of the components is quite unwieldy. Thus, a simple implementation with separate `x` and `y` components wins here - and is the right choice indeed, because extending that for part 2 is trivial.

* Part 1, Python (using complex numbers): 106 bytes, <100 ms
* Part 1, Python (using separate components): 105 bytes, <100 ms
* Part 2, Python: 114 bytes, <100 ms
