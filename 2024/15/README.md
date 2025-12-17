# 2024, Day 15: Warehouse Woes


## Solution Notes

I spend a lot of time running into dead ends and stupid bugs while implementing this. My first approach was a recursive function that checks whether it's possibe to move from one place to another, and shove boxes along, and if there's a box at the destination, recurse. That didn't work out, and while debugging, I decided to ditch the entire approach and just determine the run of boxes directly in front of the player in movement direction. If that run of boxes would be shoved into a wall, the move is invalid; otherwise, the boxes are shifted (well, actually they aren't: since my box list is a `set`, the first box is removed and the empty space behind the last box is marked as containing a box, but the effect is exactly the same).

At this point, I was expecting part 2 to be something like "the instructions are repeated in a cycle, and what's the position of the boxes after an infinite amount of time", but the twist was something entirely different, and arguable even more interesting. My run-of-boxes approach had to make way to a list (or `set`) of boxes that would be affected by a move, derived by DFS or (in my case) BFS. If any of these boxes would move into a wall if shifted in the robot's direction, the move is invalid.

During initial implementation, I was a bit too scared of the BFS part and added special-case code for left and right movements, as they could use something similar to the old run-of-boxes approach. That was exactly the wrong call &ndash; I lost a lot of time debugging this special-case horizontal movement code, and once the vertical movement code worked, I could simply remove all of it, because as it turns out, the vertical movement code _was_ already generic enough to handle horizontal movement as well ...

* Part 1, Python: 335 bytes, ~150 ms
* Part 2, Python: 436 bytes, ~600 ms
