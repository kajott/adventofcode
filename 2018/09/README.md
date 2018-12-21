# 2018, Day 9: Marble Mania

You talk to the Elves while you wait for your navigation system to initialize. To pass the time, they introduce you to their favorite [marble](https://en.wikipedia.org/wiki/Marble_(toy)) game.

## Part 1

The Elves play this game by taking turns arranging the marbles in a _circle_ according to very particular rules. The marbles are numbered starting with `0` and increasing by `1` until every marble has a number.

First, the marble numbered `0` is placed in the circle. At this point, while it contains only a single marble, it is still a circle: the marble is both clockwise from itself and counter-clockwise from itself. This marble is designated the _current marble_.

Then, each Elf takes a turn placing the _lowest-numbered remaining marble_ into the circle between the marbles that are `1` and `2` marbles _clockwise_ of the current marble. (When the circle is large enough, this means that there is one marble between the marble that was just placed and the current marble.) The marble that was just placed then becomes the _current marble_.

However, if the marble that is about to be placed has a number which is a multiple of `23`, _something entirely different happens_. First, the current player keeps the marble they would have placed, adding it to their _score_. In addition, the marble `7` marbles _counter-clockwise_ from the current marble is _removed_ from the circle and _also_ added to the current player's score. The marble located immediately _clockwise_ of the marble that was removed becomes the new _current marble_.

For example, suppose there are 9 players. After the marble with value `0` is placed in the middle, each player (shown in square brackets) takes a turn. The result of each of those turns would produce circles of marbles like this, where clockwise is to the right and the resulting current marble is in parentheses:

    [-] (0)
    [1]  0 (1)
    [2]  0 (2) 1 
    [3]  0  2  1 (3)
    [4]  0 (4) 2  1  3 
    [5]  0  4  2 (5) 1  3 
    [6]  0  4  2  5  1 (6) 3 
    [7]  0  4  2  5  1  6  3 (7)
    [8]  0 (8) 4  2  5  1  6  3  7 
    [9]  0  8  4 (9) 2  5  1  6  3  7 
    [1]  0  8  4  9  2(10) 5  1  6  3  7 
    [2]  0  8  4  9  2 10  5(11) 1  6  3  7 
    [3]  0  8  4  9  2 10  5 11  1(12) 6  3  7 
    [4]  0  8  4  9  2 10  5 11  1 12  6(13) 3  7 
    [5]  0  8  4  9  2 10  5 11  1 12  6 13  3(14) 7 
    [6]  0  8  4  9  2 10  5 11  1 12  6 13  3 14  7(15)
    [7]  0(16) 8  4  9  2 10  5 11  1 12  6 13  3 14  7 15 
    [8]  0 16  8(17) 4  9  2 10  5 11  1 12  6 13  3 14  7 15 
    [9]  0 16  8 17  4(18) 9  2 10  5 11  1 12  6 13  3 14  7 15 
    [1]  0 16  8 17  4 18  9(19) 2 10  5 11  1 12  6 13  3 14  7 15 
    [2]  0 16  8 17  4 18  9 19  2(20)10  5 11  1 12  6 13  3 14  7 15 
    [3]  0 16  8 17  4 18  9 19  2 20 10(21) 5 11  1 12  6 13  3 14  7 15 
    [4]  0 16  8 17  4 18  9 19  2 20 10 21  5(22)11  1 12  6 13  3 14  7 15 
    [5]  0 16  8 17  4 18(19) 2 20 10 21  5 22 11  1 12  6 13  3 14  7 15 
    [6]  0 16  8 17  4 18 19  2(24)20 10 21  5 22 11  1 12  6 13  3 14  7 15 
    [7]  0 16  8 17  4 18 19  2 24 20(25)10 21  5 22 11  1 12  6 13  3 14  7 15
    

The goal is to be the _player with the highest score_ after the last marble is used up. Assuming the example above ends after the marble numbered `25`, the winning score is `23+9=`_`32`_ (because player 5 kept marble `23` and removed marble `9`, while no other player got any points in this very short example game).

Here are a few more examples:

*   `10` players; last marble is worth `1618` points: high score is _`8317`_
*   `13` players; last marble is worth `7999` points: high score is _`146373`_
*   `17` players; last marble is worth `1104` points: high score is _`2764`_
*   `21` players; last marble is worth `6111` points: high score is _`54718`_
*   `30` players; last marble is worth `5807` points: high score is _`37305`_

_What is the winning Elf's score?_

Your puzzle answer was `439089`.

## Part 2

Amused by the speed of your answer, the Elves are curious:

_What would the new winning Elf's score be if the number of the last marble were 100 times larger?_

Your puzzle answer was `3668541094`.


## Solution Notes

This puzzle was a nicely put trap which I and certainly a lot other participants promptly fell into. The problem calls for a circular doubly-linked list, which is a variant of a standard data structure commonly taught in Computer Science courses, but with not enough real-world relevance to be included in common languages' standard libraries. (C++'s `std::list` is doubly-linked, but not circular, for example.) For small problem sizes, such a structure can be conveniently emulated using a simple array (i.e. a C-style array, a C++ `std::vector`, or a Python `list`). For part 1 of the puzzle, this works well enough. Since the input (and hence the problem size) is always the same for both parts, I had no qualms about taking this shortcut.

But then part 2 came and blow everything apart. Item insertion and deletion on arrays are _O(n)_ operations, making the whole puzzle _O(n²)_ when implemented this way. Instead of taking 100 times longer, it takes 10k times longer; too much to be manageable, let alone in a relatively slow language like Python!

So I had no other choice than to re-implement the whole thing with a *proper* circular doubly-linked list, after a frustating failed attempt at splitting the large list into multiple smaller sub-list (i.e. a two-level tree). For whatever reason (hey, it was 7 AM and I was tired!) I made the proper implementation in C first and only "backported" it to Python later.

_(Fun fact: Juggling around with references in (doubly-)linked lists never ceases to inflict headaches, no matter how often you implemented that already!)_

The C version is more than two orders of magnitude faster than the Python version, by the way -- so much so, that part 2 in C is twice as fast as part 1 in Python (with lists)! And that's without optimization. (Optimization didn't buy me anything, as I include the compilation time in the runtime here -- sure, `gcc -O4` generates 30% faster code, but it takes twice as long to do so ...)

* Part 1, Python (array): 204 bytes, ~500 ms
* Part 2, Python (CDLL): 276 bytes, ~30 s
* Part 2, C (CDLL): 427 bytes, ~200 ms (including compilation)
