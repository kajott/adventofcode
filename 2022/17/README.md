# 2022, Day 17: Pyroclastic Flow


## Solution Notes

Part 1 is a straightforward simulation of an almost-but-not-quite Tetris game. The most interesting question in my mind, while writing the initial non-golf version for the contest, is what part 2 is going to be. More tiles? Rotating tiles? Maybe wider playfields? It's because of the latter question that I initially used sets of `(x,y)` tuples to represent the chamber state; if I had known that part 2 is using the same 7-wide playfield, I'd have used bitfields instead, and consequently, this is what I did for the golf version. It's just soooo much more convenient.

What part 2 did ultimately turn out to be, though, is a rather nasty (if [predictable](../../2018/12)) surprise. So, it's all about finding some periodic pattern and applying it appropriately. The shortest period that can possibly emerge is certainly the length of the input (which seems to be always 10091, and hence prime) times the number of different bricks, i.e. 5. But what should this period be applied to? That's really a head-scrather, because it *not* apply to the number of blocks, for example.

What I did (and what seems to work for multiple people's inputs), is the following:
- Let the simulation run for as many blocks (_not_ time steps, curiously!) until the input has been repeated five times. (This may happen in the middle of a block simulation, but it doesn't matter.) Note the number of blocks and stack height.
- Continue the simulation until the input has been repeated another five times. The _increase_ in block count and stack height during this phase will stay the same for every subsequent run of five input cycles, so it can conveniently be used to make a projection of how high the stack will be until a bit before the 1 billion (or trillion, YMMV) block mark.
- Run the simulation for the remaining number of blocks, and add the _increase_ in stack height to the projection to get the final result.

I'm not 100% if that is the best way to do it, but it works fine for me, it's convenient enough and has good performance.

* Part 1, Python: 366 bytes, <100 ms
* Part 2, Python: 468 bytes, ~350 ms
