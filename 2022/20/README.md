# 2022, Day 20: Grove Positioning System

It's finally time to meet back up with the Elves. When you try to contact them, however, you get no reply. Perhaps you're out of range?

You know they're headed to the grove where the _star_ fruit grows, so if you can figure out where that is, you should be able to meet back up with them.

Fortunately, your handheld device has a file (your puzzle input) that contains the grove's coordinates! Unfortunately, the file is _encrypted_ - just in case the device were to fall into the wrong hands.

Maybe you can decrypt it?

When you were still back at the camp, you overheard some Elves talking about coordinate file encryption. The main operation involved in decrypting the file is called _mixing_.

## Part 1

The encrypted file is a list of numbers. To _mix_ the file, move each number forward or backward in the file a number of positions equal to the value of the number being moved. The list is _circular_, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.

For example, to move the `1` in a sequence like `4, 5, 6, _1_, 7, 8, 9`, the `1` moves one position forward: `4, 5, 6, 7, _1_, 8, 9`. To move the `-2` in a sequence like `4, _-2_, 5, 6, 7, 8, 9`, the `-2` moves two positions backward, wrapping around: `4, 5, 6, 7, 8, _-2_, 9`.

The numbers should be moved _in the order they originally appear_ in the encrypted file. Numbers moving around during the mixing process do not change the order in which the numbers are moved.

Consider this encrypted file:

    1
    2
    -3
    3
    -2
    0
    4
    

Mixing this file proceeds as follows:

    Initial arrangement:
    1, 2, -3, 3, -2, 0, 4
    
    1 moves between 2 and -3:
    2, 1, -3, 3, -2, 0, 4
    
    2 moves between -3 and 3:
    1, -3, 2, 3, -2, 0, 4
    
    -3 moves between -2 and 0:
    1, 2, 3, -2, -3, 0, 4
    
    3 moves between 0 and 4:
    1, 2, -2, -3, 0, 3, 4
    
    -2 moves between 4 and 1:
    1, 2, -3, 0, 3, 4, -2
    
    0 does not move:
    1, 2, -3, 0, 3, 4, -2
    
    4 moves between -3 and 0:
    1, 2, -3, 4, 0, 3, -2
    

Then, the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value `0`, wrapping around the list as necessary. In the above example, the 1000th number after `0` is `_4_`, the 2000th is `_-3_`, and the 3000th is `_2_`; adding these together produces `_3_`.

Mix your encrypted file exactly once. _What is the sum of the three numbers that form the grove coordinates?_

Your puzzle answer was `2827`.

## Part 2

The grove coordinate values seem nonsensical. While you ponder the mysteries of Elf encryption, you suddenly remember the rest of the decryption routine you overheard back at camp.

First, you need to apply the _decryption key_, `811589153`. Multiply each number by the decryption key before you begin; this will produce the actual list of numbers to mix.

Second, you need to mix the list of numbers _ten times_. The order in which the numbers are mixed does not change during mixing; the numbers are still moved in the order they appeared in the original, pre-mixed list. (So, if -3 appears fourth in the original list of numbers to mix, -3 will be the fourth number to move during each round of mixing.)

Using the same example as above:

    Initial arrangement:
    811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612
    
    After 1 round of mixing:
    0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153
    
    After 2 rounds of mixing:
    0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153
    
    After 3 rounds of mixing:
    0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459
    
    After 4 rounds of mixing:
    0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306
    
    After 5 rounds of mixing:
    0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459
    
    After 6 rounds of mixing:
    0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459
    
    After 7 rounds of mixing:
    0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612
    
    After 8 rounds of mixing:
    0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306
    
    After 9 rounds of mixing:
    0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306
    
    After 10 rounds of mixing:
    0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153
    

The grove coordinates can still be found in the same way. Here, the 1000th number after `0` is _`811589153`_, the 2000th is _`2434767459`_, and the 3000th is _`-1623178306`_; adding these together produces _`1623178306`_.

Apply the decryption key and mix your encrypted file ten times. _What is the sum of the three numbers that form the grove coordinates?_

Your puzzle answer was `7834270093909`.

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
