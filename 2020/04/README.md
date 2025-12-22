# [2020, Day 4: Passport Processing](https://adventofcode.com/2020/day/4)

The input consists of (typically) 280 records of 1 to 8 key-value pairs with some data. Keys are always one out of 8 possible 3-letter identifiers, values are random strings (some numeric, some hexadecimal, some 3-letter identifiers).

**Part 1** asks for how many records contain a specific set of 7 out of the 8 possible keys.

**Part 2** asks how many records not only contain these keys, but also have data matching a specific pattern in them (a number range, a number followed by one or two unit names, a hexadecimal color code, and a set of of 3-letter identifiers).


## Solution Notes

This is rather pointless drudgery instead of an intriguing puzzle. All the validations in part 2 are as bland as it gets, the only challenge is in golfing them. At 306 columns, this might be the longest line of code in my whole AoC endeavor so far.

* Part 1, Python: 160 bytes, <100 ms
* Part 2, Python: 446 bytes, <100 ms
