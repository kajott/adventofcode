# [2023, Day 25: Snowverload](https://adventofcode.com/2023/day/25)


## Solution Notes

This is a variant of the classical minimum cut problem, for which known solutions like [Karger's algorithm](https://en.wikipedia.org/wiki/Karger%27s_algorithm) and the [Stoer-Wagner algorithm](https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm) exist. I took different routes though.

My initial approach for the competition was to transform the input file into GraphViz' `neato` format. Rendering this indeed results in two chaotic ink blots connected by just three lines. The incident notes can easily be read from this graph, making the remaining job relatively easy. (Just a flood fill starting at any node and counting how many nodes have been visited and how many haven't.)

This isn't considered a proper solution though; there needs to be some way to determine the edges to cut programmatically. For this, my code iterates over all nodes in the graph and performs a full BFS starting from that node. While doing so, the number of times each edge is traversed is counted; the idea here is that the BFS *must* cross over at least one of the "critical" edges to reach the other cluster, while the internal nodes within each cluster are used more or less randomly, depending on where the starting node was. Indeed, this approach works fine: I just cut all edges that have been walked at least as much as the third-most used edge, and the clusters are neatly separated. It may be a bit too eager and cut one or two internal edges too, but since the internal nodes are very well connected, this only causes a small detour during the final flood fill and doesn't disturb the result. Performance isn't great too, but it's manageable.

* Part 1, Python: 452 bytes, ~5 s
