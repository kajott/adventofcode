# [2020, Day 5: Binary Boarding](https://adventofcode.com/2020/day/5)

The input consists of (typically) 900 strings of 10 letters, which are described as a fancy encoding of a binary address.

**Part 1** asks for the highest such address in the input.

**Part 2** asks for an address that does _not_ appear in the input, but its predecessor and successors do.


## Solution Notes

This is almost a trivial puzzle -- just a `max` operation or some simple set arithmetic, with the only special thing being the non-standard encoding of the bits.

* Part 1, Python: 99 bytes, <100 ms
* Part 2, Python: 142 bytes, <100 ms
