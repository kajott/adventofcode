# [2021, Day 4: Giant Squid](https://adventofcode.com/2021/day/4)


## Solution Notes

The main challenge here is to come up with reasonable data structures for the boards and how to check for wins. My choice is a flat 25-element list of numbers per board and a set of _indices_ of marked elements. That index set makes checking for a winning board quite easy, because a list of index sets for each row and column can be prepared and subset comparisons can be used to quickly and effortlessly check the state of a board.

For the golf versions, this requires some fancy packing; in effect, I just made each board a flat list and put the index set at the 26th slot in each board, as that is reasonably efficient to access. Parsing the file also requires some gymnastics; tedious, but not really challenging.

One annoying element of part 1 is that the program must terminate immediately after the first winning board has been found, which is typically in a nested loop where you can't just `break` out of. The golf version solves this by just simulating the whole drawing process, until the very end, making a note of the first winning score and discarding everything after that.

In that sense, part 2 is even easier, but additional care has to be taken to eliminate winning boards from further draw processes, as they will otherwise be "won" again for every subsequent draw.

* Part 1, Python: 342 bytes, <100 ms
* Part 2, Python: 352 bytes, <100 ms
