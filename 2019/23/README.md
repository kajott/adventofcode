# 2019, Day 23: Category Six


## Solution Notes

A nice and simple puzzle with no unpleasant surprises.

For golfing, I first did the obvious thing and turned the 50 machines into class instances. For the second revision, I put all the machine state (IP and RB registers, input and output queue) into the main memory dictionary at addresses `-1` to `-4`, which is safe because negative addresses are otherwise forbidden by the Intcode spec. This makes register and queue access slighly longer (`X.p` becomes `X[-1]`, +1 byte), but this is far outweighed by the shorter memory accesses (`X.m[i]` -> `X[i]`, -2 bytes) and instantiation.

* Part 1, Python (machines as classes): 690 bytes, ~150 ms
* Part 1, Python (machines as dictionaries): 668 bytes, ~150 ms
* Part 2, Python: 738 bytes, ~1 s
