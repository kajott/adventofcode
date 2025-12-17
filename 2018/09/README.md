# 2018, Day 9: Marble Mania


## Solution Notes

This puzzle was a nicely put trap which I and certainly a lot other participants promptly fell into. The problem calls for a circular doubly-linked list, which is a variant of a standard data structure commonly taught in Computer Science courses, but with not enough real-world relevance to be included in common languages' standard libraries. (C++'s `std::list` is doubly-linked, but not circular, for example.) For small problem sizes, such a structure can be conveniently emulated using a simple array (i.e. a C-style array, a C++ `std::vector`, or a Python `list`). For part 1 of the puzzle, this works well enough. Since the input (and hence the problem size) is always the same for both parts, I had no qualms about taking this shortcut.

But then part 2 came and blow everything apart. Item insertion and deletion on arrays are _O(n)_ operations, making the whole puzzle _O(n²)_ when implemented this way. Instead of taking 100 times longer, it takes 10k times longer; too much to be manageable, let alone in a relatively slow language like Python!

So I had no other choice than to re-implement the whole thing with a *proper* circular doubly-linked list, after a frustrating failed attempt at splitting the large list into multiple smaller sub-list (i.e. a two-level tree). For whatever reason (hey, it was 7 AM and I was tired!) I made the proper implementation in C first and only "backported" it to Python later.

_(Fun fact: Juggling around with references in (doubly-)linked lists never ceases to inflict headaches, no matter how often you implemented that already!)_

The C version is more than two orders of magnitude faster than the Python version, by the way -- so much so, that part 2 in C is twice as fast as part 1 in Python (with lists)! And that's without optimization. (Optimization didn't buy me anything, as I include the compilation time in the runtime here -- sure, `gcc -O4` generates 30% faster code, but it takes twice as long to do so ...)

* Part 1, Python (array): 204 bytes, ~500 ms
* Part 2, Python (CDLL): 276 bytes, ~30 s
* Part 2, C (CDLL): 427 bytes, ~200 ms (including compilation)
