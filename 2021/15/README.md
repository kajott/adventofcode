# 2021, Day 15: Chiton

You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in [chitons](https://en.wikipedia.org/wiki/Chiton), and it would be best not to bump any of them.

## Part 1

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of _risk level_ throughout the cave (your puzzle input). For example:

    1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581
    

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its _risk level_; to determine the total risk of an entire path, add up the risk levels of each position you _enter_ (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the _lowest total risk_. In this example, a path with the lowest total risk is highlighted here:

    1.........
    1.........
    2136511...
    ......15..
    .......1..
    .......13.
    ........2.
    ........3.
    ........21
    .........1
    

The total risk of this path is _`40`_ (the starting position is never entered, so its risk is not counted).

_What is the lowest total risk of any path from the top left to the bottom right?_

Your puzzle answer was `811`.

## Part 2

Now that you know how to find low-risk paths in the cave, you can try to find your way out.

The entire cave is actually _five times larger in both dimensions_ than you thought; the area you originally scanned is just one tile in a 5x5 tile area that forms the full map. Your original map tile repeats to the right and downward; each time the tile repeats to the right or downward, all of its risk levels _are 1 higher_ than the tile immediately up or left of it. However, risk levels above `9` wrap back around to `1`. So, if your original map had some position with a risk level of `8`, then that same position on each of the 25 total tiles would be as follows:

    8 9 1 2 3
    9 1 2 3 4
    1 2 3 4 5
    2 3 4 5 6
    3 4 5 6 7
    

Each single digit above corresponds to the example position with a value of `8` on the top-left tile. Because the full map is actually five times larger in both dimensions, that position appears a total of 25 times, once in each duplicated tile, with the values shown above.

Here is the full five-times-as-large version of the first example above, with the repetitions marked:

    1163751742|2274862853|3385973964|4496184175|5517295286
    1381373672|2492484783|3513595894|4624616915|5735727126
    2136511328|3247622439|4358733541|5469844652|6571955763
    3694931569|4715142671|5826253782|6937364893|7148475914
    7463417111|8574528222|9685639333|1796741444|2817852555
    1319128137|2421239248|3532341359|4643452461|5754563572
    1359912421|2461123532|3572234643|4683345754|5794456865
    3125421639|4236532741|5347643852|6458754963|7569865174
    1293138521|2314249632|3425351743|4536462854|5647573965
    2311944581|3422155692|4533266713|5644377824|6755488935
    ----------+----------+----------+----------+----------
    2274862853|3385973964|4496184175|5517295286|6628316397
    2492484783|3513595894|4624616915|5735727126|6846838237
    3247622439|4358733541|5469844652|6571955763|7682166874
    4715142671|5826253782|6937364893|7148475914|8259586125
    8574528222|9685639333|1796741444|2817852555|3928963666
    2421239248|3532341359|4643452461|5754563572|6865674683
    2461123532|3572234643|4683345754|5794456865|6815567976
    4236532741|5347643852|6458754963|7569865174|8671976285
    2314249632|3425351743|4536462854|5647573965|6758684176
    3422155692|4533266713|5644377824|6755488935|7866599146
    ----------+----------+----------+----------+----------
    3385973964|4496184175|5517295286|6628316397|7739427418
    3513595894|4624616915|5735727126|6846838237|7957949348
    4358733541|5469844652|6571955763|7682166874|8793277985
    5826253782|6937364893|7148475914|8259586125|9361697236
    9685639333|1796741444|2817852555|3928963666|4139174777
    3532341359|4643452461|5754563572|6865674683|7976785794
    3572234643|4683345754|5794456865|6815567976|7926678187
    5347643852|6458754963|7569865174|8671976285|9782187396
    3425351743|4536462854|5647573965|6758684176|7869795287
    4533266713|5644377824|6755488935|7866599146|8977611257
    ----------+----------+----------+----------+----------
    4496184175|5517295286|6628316397|7739427418|8841538529
    4624616915|5735727126|6846838237|7957949348|8168151459
    5469844652|6571955763|7682166874|8793277985|9814388196
    6937364893|7148475914|8259586125|9361697236|1472718347
    1796741444|2817852555|3928963666|4139174777|5241285888
    4643452461|5754563572|6865674683|7976785794|8187896815
    4683345754|5794456865|6815567976|7926678187|8137789298
    6458754963|7569865174|8671976285|9782187396|1893298417
    4536462854|5647573965|6758684176|7869795287|8971816398
    5644377824|6755488935|7866599146|8977611257|9188722368
    ----------+----------+----------+----------+----------
    5517295286|6628316397|7739427418|8841538529|9952649631
    5735727126|6846838237|7957949348|8168151459|9279262561
    6571955763|7682166874|8793277985|9814388196|1925499217
    7148475914|8259586125|9361697236|1472718347|2583829458
    2817852555|3928963666|4139174777|5241285888|6352396999
    5754563572|6865674683|7976785794|8187896815|9298917926
    5794456865|6815567976|7926678187|8137789298|9248891319
    7569865174|8671976285|9782187396|1893298417|2914319528
    5647573965|6758684176|7869795287|8971816398|9182927419
    6755488935|7866599146|8977611257|9188722368|1299833479
    

Equipped with the full map, you can now find a path from the top left corner to the bottom right corner with the lowest total risk:

    1................................................
    1.................................................
    2.................................................
    3.................................................
    7.................................................
    1.................................................
    1.................................................
    3.................................................
    1.................................................
    2.................................................
    2.................................................
    2.................................................
    324...............................................
    ..15..............................................
    ...4..............................................
    ...1..............................................
    ...1123532........................................
    .........1........................................
    .........2342.....................................
    ............332...................................
    ..............1...................................
    ..............61..................................
    ...............44.................................
    ................4.................................
    ................1.................................
    ................2461..............................
    ...................4..............................
    ...................3..............................
    ...................4564...........................
    ......................554.........................
    ........................3163......................
    ...........................2......................
    ...........................8......................
    ...........................125....................
    .............................6413.................
    ................................7.................
    ................................26................
    .................................21...............
    ..................................7...............
    ..................................6112............
    .....................................5............
    .....................................4............
    .....................................1............
    .....................................34725........
    .........................................3........
    .........................................2........
    .........................................24.......
    ..........................................1431....
    .............................................2....
    .............................................33479
    

The total risk of this path is _`315`_ (the starting position is still never entered, so its risk is not counted).

Using the full map, _what is the lowest total risk of any path from the top left to the bottom right?_

Your puzzle answer was `3012`.


## Solution Notes

Part 1 is nicely solvable using Dynamic Programming, i.e. incrementally preparing a table with the cost of the the optimal path to each cell, coming from either above or the left.

Part 2, however, is quite tricky: What the task description and even the example dataset doesn't say is that it's perfectly possible that there's a slightly better path through the maze when going up or left at some places instead of just down or right. So, in the end, BFS is the algorithm to use. Since the maze is so big, that is horribly slow, but it gets the job done ... just barely.

* Part 1, Python: 199 bytes, <100 ms
* Part 2, Python: 376 bytes, ~7 s
