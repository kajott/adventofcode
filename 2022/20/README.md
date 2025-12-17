# 2022, Day 20: Grove Positioning System


## Solution Notes

This is technically a very simple task, but getting the index arithmetics just right took me an inordinate amount of time. The trick is to remove the element from the list immediately and consider it as "floating", and then compute the new index (modulo N-1 instead of N, because the list is temporarily shorter than it used to be) and reinsert it.

Keeping track of the original order of the elements is another tricky thing; not because it's hard to figure out how to do it, but because it's not trivial to do it _efficiently_. My original idea was to just assign a number tag to each value and work through elements in order of the tag. That's all fine, but it takes a high tax on runtime, as it's essentially another nested search loop. This is fast in PyPy, but slow as molasses in CPython.

Another idea is to put the numbers into little classes that build a linked list. The main data list is still a plain list of numbers (or rather, number class instances), but there's no need to search for the next item. This brings runtime down one tenth of what it used to be at a moderate code size increase, but there's a caveat: `list.index()` for class instances is _extremely_ slow on CPython 2.7, which is the default interpreter I use over here. It's even slower than the nested loop code! It seems to be missing a major optimization that was added somewhere between 2.7 and 3.10, and that's why my implementations of that approach run in Python 3 for a change.

Finally, there's a third approach that's worthwhile: Indirect addressing, or as I call it, "order tables". This keeps the number array intact at all times, but defines an additional array with indexes into the number array. This is initialized with a simple counter sequence, and _this_ is where the sorting operations are performed. This approach performs extremely well (faster than all others) *and* requires very little code to boot. Even a combined solution of parts 1 and 2 is smaller than any of the single-part solutions of the other approaches!

Golfed C implementations of the linked list and order table approaches (that even perform two `memmove`s per item to save on code size) run both parts in a quarter of a second, including compilation.

* Part 1, Python (nested loop): 223 bytes, ~2 s
* Part 2, Python (nested loop): 266 bytes, ~20 s
* Part 1, Python (linked list): 241 bytes, ~150 ms
* Part 2, Python (linked list): 277 bytes, ~2 s
* Part 1, Python (order table): 170 bytes, <100 ms
* Part 2, Python (order table): 189 bytes, ~1.5 s
* Parts 1+2, Python (order table): 220 bytes, ~1.5 s
* Parts 1+2, C (linked list): 614 bytes, ~600 ms
* Parts 1+2, C (order table): 519 bytes, ~200 ms
