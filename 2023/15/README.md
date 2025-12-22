# [2023, Day 15: Lens Library](https://adventofcode.com/2023/day/15)

The input consists of (typically) 4000 short random alphanumeric and symbolic strings of lengths 4 to 8.

The task defines a simple hash function of the type `((h+x)*17)&255`.

**Part 1** asks about the hashes of all the strings.

For part 2, the strings are revealed to have a meaning: They are instructions, consisting of an alphanumeric name, a symbol denoting one of two operations, and optionally a single-digit number. The name is to be hashed to compute which of 256 "boxes" the operation applies to. Each box can contain any number of objects with their name and an associated number, in a specified order. One of the operations removes the named element from its box. The other operation adds the element to its box, with the specified number; if it already exists in the box, its existing number is changed to the newly-specified number.

**Part 2** asks for some checksum number representing the state of all the boxes after executing all the instructions.


## Solution Notes

Completely straightforward. Implement as described, and be done with it; no hidden traps.

* Part 1, Python: 110 bytes, <100 ms
* Part 2, Python: 290 bytes, <100 ms
