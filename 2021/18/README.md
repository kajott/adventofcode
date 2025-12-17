# 2021, Day 18: Snailfish


## Solution Notes

There's no major pitfalls in this puzzle, except that it's just a tedious and boring ... well, homework. One might be tempted to implement this using nested lists (because that's what they are, right?), but searching for neighboring scalar values across all hierarchy levels as part of the explode operation is a highly complex operation itself, so I just "flattened" the lists with special sentinel values for `[` and `]` and omitting `,`. That works quite well, though I'm not at all sure whether it's the best way to do things. That's especially true for the golf versions.

* Part 1, Python: 560 bytes, ~350 ms
* Part 2, Python: 622 bytes, ~4 s
