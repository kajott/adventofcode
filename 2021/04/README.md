# 2021, Day 4: Giant Squid

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you _can_ see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play [bingo](https://en.wikipedia.org/wiki/Bingo_(American_version))?

## Part 1

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is _marked_ on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board _wins_. (Diagonals don't count.)

The submarine has a _bingo subsystem_ to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    
    22 13 17 11  0
     8  2 23  4 24
    21  9 14 16  7
     6 10  3 18  5
     1 12 20 15 19
    
     3 15  0  2 22
     9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6
    
    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
     2  0 12  3  7
    

After the first five numbers are drawn (`7`, `4`, `9`, `5`, and `11`), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
     8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
     6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
     1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    

After the next six numbers are drawn (`17`, `23`, `2`, `0`, `14`, and `21`), there are still no winners:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
     8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
     6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
     1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    

Finally, `24` is drawn:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
     8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
     6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
     1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
    

At this point, the third board _wins_ because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: `_14 21 17 24 4_`).

The _score_ of the winning board can now be calculated. Start by finding the _sum of all unmarked numbers_ on that board; in this case, the sum is `188`. Then, multiply that sum by _the number that was just called_ when the board won, `24`, to get the final score, `188 * 24 = `_`4512`_.

To guarantee victory against the giant squid, figure out which board will win first. _What will your final score be if you choose that board?_

Your puzzle answer was `16716`.

## Part 2

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to _figure out which board will win last_ and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after `13` is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to `148` for a final score of `148 * 13 = `_`1924`_.

Figure out which board will win last. _Once it wins, what would its final score be?_

Your puzzle answer was `4880`.


## Solution Notes

The main challenge here is to come up with reasonable data structures for the boards and how to check for wins. My choice is a flat 25-element list of numbers per board and a set of _indices_ of marked elements. That index set makes checking for a winning board quite easy, because a list of index sets for each row and column can be prepared and subset comparisons can be used to quickly and effortlessly check the state of a board.

For the golf versions, this requires some fancy packing; in effect, I just made each board a flat list and put the index set at the 26th slot in each board, as that is reasonably efficient to access. Parsing the file also requires some gymnastics; tedious, but not really challenging.

One annoying element of part 1 is that the program must terminate immediately after the first winning board has been found, which is typically in a nested loop where you can't just `break` out of. The golf version solves this by just simulating the whole drawing process, until the very end, making a note of the first winning score and discarding everything after that.

In that sense, part 2 is even easier, but additional care has to be taken to eliminate winning boards from further draw processes, as they will otherwise be "won" again for every subsequent draw.

* Part 1, Python: 342 bytes, <100 ms
* Part 2, Python: 352 bytes, <100 ms
