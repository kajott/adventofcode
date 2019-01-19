# 2016, Day 22: Grid Computing

## Part 1

You gain access to a massive storage cluster arranged in a grid; each storage node is only connected to the four nodes directly adjacent to it (three if the node is on an edge, two if it's in a corner).

You can directly access data _only_ on node `/dev/grid/node-x0-y0`, but you can perform some limited actions on the other nodes:

*   You can get the disk usage of all nodes (via [`df`](https://en.wikipedia.org/wiki/Df_(Unix)#Example)). The result of doing this is in your puzzle input.
*   You can instruct a node to _move_ (not copy) _all_ of its data to an adjacent node (if the destination node has enough space to receive the data). The sending node is left empty after this operation.

Nodes are named by their position: the node named `node-x10-y10` is adjacent to nodes `node-x9-y10`, `node-x11-y10`, `node-x10-y9`, and `node-x10-y11`.

Before you begin, you need to understand the arrangement of data on these nodes. Even though you can only move data between directly connected nodes, you're going to need to rearrange a lot of the data to get access to the data you need. Therefore, you need to work out how you might be able to shift data around.

To do this, you'd like to count the number of _viable pairs_ of nodes. A viable pair is any two nodes (A,B), _regardless of whether they are directly connected_, such that:

*   Node A is _not_ empty (its `Used` is not zero).
*   Nodes A and B are _not the same_ node.
*   The data on node A (its `Used`) _would fit_ on node B (its `Avail`).

_How many viable pairs_ of nodes are there?

Your puzzle answer was `1007`.

## Part 2

Now that you have a better understanding of the grid, it's time to get to work.

Your goal is to gain access to the data which begins in the node with `y=0` and the _highest `x`_ (that is, the node in the top-right corner).

For example, suppose you have the following grid:

    Filesystem            Size  Used  Avail  Use%
    /dev/grid/node-x0-y0   10T    8T     2T   80%
    /dev/grid/node-x0-y1   11T    6T     5T   54%
    /dev/grid/node-x0-y2   32T   28T     4T   87%
    /dev/grid/node-x1-y0    9T    7T     2T   77%
    /dev/grid/node-x1-y1    8T    0T     8T    0%
    /dev/grid/node-x1-y2   11T    7T     4T   63%
    /dev/grid/node-x2-y0   10T    6T     4T   60%
    /dev/grid/node-x2-y1    9T    8T     1T   88%
    /dev/grid/node-x2-y2    9T    6T     3T   66%
    

In this example, you have a storage grid `3` nodes wide and `3` nodes tall. The node you can access directly, `node-x0-y0`, is almost full. The node containing the data you want to access, `node-x2-y0` (because it has `y=0` and the highest `x` value), contains 6 [terabytes](https://en.wikipedia.org/wiki/Terabyte) of data - enough to fit on your node, if only you could make enough space to move it there.

Fortunately, `node-x1-y1` looks like it has enough free space to enable you to move some of this data around. In fact, it seems like all of the nodes have enough space to hold any node's data (except `node-x0-y2`, which is much larger, very full, and not moving any time soon). So, initially, the grid's capacities and connections look like this:

    ( 8T/10T) --  7T/ 9T -- [ 6T/10T]
        |           |           |
      6T/11T  --  0T/ 8T --   8T/ 9T
        |           |           |
     28T/32T  --  7T/11T --   6T/ 9T
    

The node you can access directly is in parentheses; the data you want starts in the node marked by square brackets.

In this example, most of the nodes are interchangable: they're full enough that no other node's data would fit, but small enough that their data could be moved around. Let's draw these nodes as `.`. The exceptions are the empty node, which we'll draw as `_`, and the very large, very full node, which we'll draw as `#`. Let's also draw the goal data as `G`. Then, it looks like this:

    (.) .  G
     .  _  .
     #  .  .
    

The goal is to move the data in the top right, `G`, to the node in parentheses. To do this, we can issue some commands to the grid and rearrange the data:

*   Move data from `node-y0-x1` to `node-y1-x1`, leaving node `node-y0-x1` empty:
    
        (.) _  G
         .  .  .
         #  .  .
        
    
*   Move the goal data from `node-y0-x2` to `node-y0-x1`:
    
        (.) G  _
         .  .  .
         #  .  .
        
    
*   At this point, we're quite close. However, we have no deletion command, so we have to move some more data around. So, next, we move the data from `node-y1-x2` to `node-y0-x2`:
    
        (.) G  .
         .  .  _
         #  .  .
        
    
*   Move the data from `node-y1-x1` to `node-y1-x2`:
    
        (.) G  .
         .  _  .
         #  .  .
        
    
*   Move the data from `node-y1-x0` to `node-y1-x1`:
    
        (.) G  .
         _  .  .
         #  .  .
        
    
*   Next, we can free up space on our node by moving the data from `node-y0-x0` to `node-y1-x0`:
    
        (_) G  .
         .  .  .
         #  .  .
        
    
*   Finally, we can access the goal data by moving the it from `node-y0-x1` to `node-y0-x0`:
    
        (G) _  .
         .  .  .
         #  .  .
        
    

So, after `7` steps, we've accessed the data we want. Unfortunately, each of these moves takes time, and we need to be efficient:

_What is the fewest number of steps_ required to move your goal data to `node-x0-y0`?

Your puzzle answer was `242`.


## Solution Notes

Part 2 is a pure smoke an mirrors affair. What looks like a typical BFS problem quickly blows apart because of the sheer problem size. The problem can only be reasonably solved by ~~cheating~~ making use of some specific properties of the input data, some of which are hinted at in the puzzle description:

* There's indeed only three types of nodes: Those which are somewhat full, those which are too big to be moved (and can thus be regarded as "walls" while traversing the grid), and exactly one empty node which is basically the "cursor".
* The normal nodes' capacity and fill level are chosen so that they really are totally transparent: their minimum capacity is less than their maximum fill level, so there's never a situation where data can't be moved from one node into the empty one.
* For all users, the "wall"-type nodes form a single line; specifically, a barrier that's at some `y` position between the empty node and the top of the grid, and extend from some `x` position (which is generally left of the cursor) up to the right edge.

In other words, the whole stuff about capacities is just smore and mirrors. In the end, it's a simple sliding puzzle that can (only?) be solved by exploiting this and walking through the grid with the "cursor" (i.e. the empty node):

* Go up until the barrier.
* Go left until the end of the barrier.
* Go up.
* Go right. The final move to the right pushes the target data one grid cell left.
* Circle around to move the target data left, one grid cell at a time. Each cell takes 5 moves (down, left, left, up, right).

The whole thing fits into a trivial formula with only the grid width, cursor position and barrier start `x` coordinate as an input. (The `y` position of the barrier doesn't even matter.)

* Part 1, Python: 142 bytes, ~200 ms
* Part 2, Python: 181 bytes, <100 ms
