# [2017, Day 7: Recursive Circus](https://adventofcode.com/2017/day/7)


## Solution Notes

Part 1 is quite easy (you can even ignore the weights altogether), part 2 requires some wrapping your head around what exactly is requested. Initially, I just detected imbalances while traversing the tree and output the weight of the majority of the children -- that's not sufficient! The question is rather to which value the base weight of the outlier child needed to be adjusted. This required some more nested table lookups -- `table1[table2[table3[0][1]][0]]` is quite something, isn't it?

* Part 1, Python: 128 bytes, <100 ms
* Part 2, Python: 383 bytes, <100 ms
