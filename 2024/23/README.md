# [2024, Day 23: LAN Party](https://adventofcode.com/2024/day/23)

The input descibes an acyclic graph with (typically) 3500 edges.

**Part 1** asks how many sets of three mutually connected nodes are in the graph.

**Part 2** asks for the largest set of connected nodes.


## Solution Notes

A nice graph problem. I fell intro a trap early in part 1 in that I counted also indirectly connected nodes (i.e. if there's `A-B` and `B-C`, I assumed `A-C` too), resulting in much more triples than there actually were.

Part 2 is technically the [maximum clique problem](https://en.wikipedia.org/wiki/Clique_problem), which is NP-complete and hence sounds very scary. But in fact, it isn't at all, at least not for the inputs we've been given: For each node, consider this node part of a clique, and then add that node's adjacent nodes to the clique iff they are also adjacent to all existing nodes in the clique. This gives the answer in no time and with even less code than part 1.

* Part 1, Python: 257 bytes, <100 ms
* Part 2, Python: 241 bytes, <100 ms
