# [2022, Day 6: Tuning Trouble](https://adventofcode.com/2022/day/6)

The input consists of a (typically) 4096-bytestring of random lowercase characters.

**Part 1** asks for the first position of a 4-character substring that doesn't contain any repeated characters in it.

**Part 2** asks the same, but for a substring of **14** characters.


## Solution Notes

This task is almost comically easy; the only prerequisite is understanding how to use sets. The difference between parts 1 and 2 is just a parameter that increases runtime by a mere factor of seven. I guess that for people who tried to solve part 1 in terms of mere comparisons (i.e. `a!=b and a!=c and a!=d and b!=c and b!=d and c!=d`), part 2 might have been a nastier surprise.

The x86 DOS version is also very compact this time. It uses a small histogram of 32 bins (enough to tell letters apart) that counts how often each byte / letter has been seen in the previous N (with N=4 or N=14) characters. The histogram is only updated at the "head" when a new byte is examined, and later at the "tail", which is always N bytes behind the head and decrements the histogram bins again. Every time a histogram bin changes its value from or to zero, a second counter is incremented or decremented; effectively, this counter tells how many histogram bins are non-zero, i.e. how many distinct characters are found in the last N bytes. If that number reaches N, we've found a match.

* Part 1, Python: 86 bytes, <100 ms
* Part 2, Python: 88 bytes, <100 ms
* Parts 1+2, x86 DOS Assembly: 142 bytes (assembled)
