# 2016, Day 16: Dragon Checksum

You're done scanning this part of the network, but you've left traces of your presence. You need to overwrite some disks with random-looking data to cover your tracks and update the local security system with a new checksum for those disks.

For the data to not be suspicious, it needs to have certain properties; purely random data will be detected as tampering. To generate appropriate random data, you'll need to use a modified [dragon curve](https://en.wikipedia.org/wiki/Dragon_curve).

## Part 1

Start with an appropriate initial state (your puzzle input). Then, so long as you don't have enough data yet to fill the disk, repeat the following steps:

*   Call the data you have at this point "a".
*   Make a copy of "a"; call this copy "b".
*   Reverse the order of the characters in "b".
*   In "b", replace all instances of `0` with `1` and all `1`s with `0`.
*   The resulting data is "a", then a single `0`, then "b".

For example, after a single step of this process,

*   `1` becomes `100`.
*   `0` becomes `001`.
*   `11111` becomes `11111000000`.
*   `111100001010` becomes `1111000010100101011110000`.

Repeat these steps until you have enough data to fill the desired disk.

Once the data has been generated, you also need to create a checksum of that data. Calculate the checksum _only_ for the data that fits on the disk, even if you generated more data than that in the previous step.

The checksum for some given data is created by considering each non-overlapping _pair_ of characters in the input data. If the two characters match (`00` or `11`), the next checksum character is a `1`. If the characters do not match (`01` or `10`), the next checksum character is a `0`. This should produce a new string which is exactly half as long as the original. If the length of the checksum is _even_, repeat the process until you end up with a checksum with an _odd_ length.

For example, suppose we want to fill a disk of length `12`, and when we finally generate a string of at least length `12`, the first `12` characters are `110010110100`. To generate its checksum:

*   Consider each pair: `11`, `00`, `10`, `11`, `01`, `00`.
*   These are same, same, different, same, different, same, producing `110101`.
*   The resulting string has length `6`, which is _even_, so we repeat the process.
*   The pairs are `11` (same), `01` (different), `01` (different).
*   This produces the checksum `100`, which has an _odd_ length, so we stop.

Therefore, the checksum for `110010110100` is `100`.

Combining all of these steps together, suppose you want to fill a disk of length `20` using an initial state of `10000`:

*   Because `10000` is too short, we first use the modified dragon curve to make it longer.
*   After one round, it becomes `10000011110` (`11` characters), still too short.
*   After two rounds, it becomes `10000011110010000111110` (`23` characters), which is enough.
*   Since we only need `20`, but we have `23`, we get rid of all but the first `20` characters: `10000011110010000111`.
*   Next, we start calculating the checksum; after one round, we have `0111110101`, which `10` characters long (_even_), so we continue.
*   After two rounds, we have `01100`, which is `5` characters long (_odd_), so we are done.

In this example, the correct checksum would therefore be `01100`.

The first disk you have to fill has length `272`. Using the initial state in your puzzle input, _what is the correct checksum_?

Your puzzle input was `10010000000110000`.

Your puzzle answer was `10010110010011110`.

## Part 2

The second disk you have to fill has length `35651584`. Again using the initial state in your puzzle input, _what is the correct checksum_ for this disk?

Your puzzle input was still `10010000000110000`.

Your puzzle answer was `01101011101100011`.


## Solution Notes

A rather simple puzzle, but surprisingly slow to compute in Python.

I learned the most interesting lesson when implementing part 2 in C (to make it faster, and because it's fun and simple): It took almost a second to compile and run, and the binary was over 70 megabytes large! The size part is understandable -- I had a large (70M elements) string with a short initializer, so the linker could no longer put it into `.bss` and had to write all 70M zeroes into the `.data` segment. The more interesting issue at hand is that the GNU linker was really, really slow at this! Anyway, after splitting the declaration and the initialization (the latter being a simple `strcpy` at the start of the program), the binary shrunk to 8k and run in about 100 milliseconds, computation included -- that's more what I expected.

Because the code is so simple, I even wrote an Linux-on-x86_64 assembly version, but this didn't offer any tangible gains compared to C. Nevertheless, it was a fun exercise!

* Part 1, Python: 173 bytes, <100 ms
* Part 2, Python: 180 bytes, ~10 s
* Part 2, C: 326 bytes, ~150 ms
* Part 2, Assembler: ~150 ms
