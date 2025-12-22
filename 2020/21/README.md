# [2020, Day 21: Allergen Assessment](https://adventofcode.com/2020/day/21)

The input consists of (typically) 30 lines, each with ca. 10 random 4-to-9-letter words ("ingredients"), plus "allergen" information in plain English (e.g. `contains fish, peanuts, eggs`). The allergen lists are incomplete: there may be additional allergens in each line.

The task is to find out which random word corresponds to which plain-English allergen.

**Part 1** asks how many ingredients are _not_ allergens.

**Part 2** asks for the mapping of the English allergen names to their random-letter-word counterparts.


## Solution Notes

The hardest part of this puzzle is understanding the extremely confusing task description, and deducing that (a) the whole thing is all about what was already done in the second half of part 2 of [day 16](../16), and that (b) a full solution is already required to answer part 1. (At least, I'm not aware of a possible shortcut.) Because of this, I put both parts into one program, as the only difference would be the `print` statement at the very end.

* Parts 1+2, Python: 341 bytes, <100 ms
