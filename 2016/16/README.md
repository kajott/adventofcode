# 2016, Day 16: Dragon Checksum


## Solution Notes

A rather simple puzzle, but surprisingly slow to compute in Python.

I learned the most interesting lesson when implementing part 2 in C (to make it faster, and because it's fun and simple): It took almost a second to compile and run, and the binary was over 70 megabytes large! The size part is understandable -- I had a large (70M elements) string with a short initializer, so the linker could no longer put it into `.bss` and had to write all 70M zeroes into the `.data` segment. The more interesting issue at hand is that the GNU linker was really, really slow at this! Anyway, after splitting the declaration and the initialization (the latter being a simple `strcpy` at the start of the program), the binary shrunk to 8k and run in about 100 milliseconds, computation included -- that's more what I expected.

Because the code is so simple, I even wrote an Linux-on-x86_64 assembly version, but this didn't offer any tangible gains compared to C. Nevertheless, it was a fun exercise!

* Part 1, Python: 173 bytes, <100 ms
* Part 2, Python: 180 bytes, ~10 s
* Part 2, C: 326 bytes, ~150 ms
* Part 2, Assembler: ~150 ms
