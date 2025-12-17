# 2024, Day 5: Print Queue


## Solution Notes

The important part of this task is to **not** overthink it: While it might seem like this puzzle is about topological ordering, this approach will lead to some suffering because the rules themselves aren't cycle-free, only the rules exercised by each _update_ are. (Luckily, I did _not_ learn that the hard way; I just heard from other users who fell into this trap.)

The actually recommended way of doing things is as blunt as it gets: For each update, check the list of pages against all the rules. If all checks pass, it's a result for part 1; if they don't, swap the offending elements and repeat the entire checking process until the list stabilizes (which it always does, eventually) to get the result for part 2.

The slightly annoying aspect of this puzzle is indeed input parsing, at least as far as code golf is concerned. The approach that works best for part 1 (in the sense of "least amount of code") isn't really suitable for part 2, so I ended up with completely different ways of handling input between the parts.

* Part 1, Python: 199 bytes, ~150 ms
* Part 2, Python: 283 bytes, ~300 ms
* Parts 1+2, Python: 299 bytes, ~300 ms
