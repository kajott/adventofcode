# [2021, Day 23: Amphipod](https://adventofcode.com/2021/day/23)

The task is about a simulation of objects moving around on a small maze-like map that consists of an 11-cell long (initially empty) hallway with four side rooms attached at cells 3, 5, 7 and 9. These side rooms are 2 cells deep; each initially contains two objects identified by letters `A` to `D` (the input).

Objects can be moved in any cardinal direction, but with different costs per step: `A` has a cost of 1, `B` 10, `C` 100 and `D` 1000. The goal is to re-arrange the objects such that the first room contains all `A`s, the second room all `B`s, etc. There are several restrictions to object movement; in essence, objects may only move into the hallway once and then go to their destination room. Objects also must not block the hallway entrance.

**Part 1** asks for the minimum cost to reach the goal.

**Part 2** asks the same, but it increases the size of the rooms to 4 and populates them with a fixed set of 4x2 new objects.


## Solution Notes

Technically, this puzzle just a standard Dijkstra graph search, but the devil is in the details. My first approach was to simply generate all valid moves for all objects, using a rather complicated distance table. This solves part 1 in about 20 seconds, but is totally untenable for part 2: I stopped the program after 1 hour, at which point it was at roughly half the expected cost ("energy"). It would have taken many more hours to finish, because the algorithm is approaching the target cost only asymptotically.

Long story short, the move generator function really needs to take all the special cases into account, otherwise it will be far too slow for part 2. The following observations help:
- Amphipods that enter a room will always go all the way to the bottommost slot and stay there forever. Leaving that place would be just a waste of energy, because all it could do there is linger around in the hallway (blocking it for other amphipods) and then return where it came from. \
  As a result, the occupancy state of each room can be split into a list of "foreign" amphipods (which will leave the room at some point) and a simple _count_ of "correct" amphipods at the bottom.
- The rule that amphipods can't move freely inside the hallway means that every amphipod is only making at most two moves throughout the whole game: One (optional) move into the hallway, and one into its final location.
- Of all amphipods in a room, only the topmost one can actually move anywhere. (Yes, this is obvious, but it cuts down the search space *a lot*!)
- There are only three types of moves possible at all:
  - Amphipods in a hallway can move to the bottom of their room if there are no foreign amphipods there and the path is clear.
  - The topmost foreign amphipods in a room can move into any reachable spot of the hallway.
  - The topmost foreign amphipods can move directly into their target room if it's free of foreign amphipods and the path across the hallway is clear.

With these restrictions, runtime can be reduced into the sub-3-second range for both parts; the complicated part is getting everything just right, as the slightest implementation bug will just produce a wrong result with no proper ways of debugging.

And then there's the whole golf situation ... I transcribed my non-golf solution almost literally, with the exception that instead of classes and nicely-named members, the game state is encoded in a single tuple that contains
- the number of correct amphipods in each room
- the number of foreign amphipods in each room
- the types of foreign amphipods in each room
- occupancy of the seven possible spots in the hallway

The end result is pretty damn close to the kibibyte mark, and I'm sure that by changing the approach a bit, more savings would be possible, but I'm quite satisfied anyway.

* Part 1, Python: 982 bytes, ~2.5 s
* Part 2, Python: 1000 bytes, ~2.5 s
