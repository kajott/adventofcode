# 2021, Day 23: Amphipod

A group of [amphipods](https://en.wikipedia.org/wiki/Amphipoda) notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, "surely you can help us with a question that has stumped our best scientists."

## Part 1

They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: _Amber_ (`A`), _Bronze_ (`B`), _Copper_ (`C`), and _Desert_ (`D`). They live in a burrow that consists of a _hallway_ and four _side rooms_. The side rooms are initially full of amphipods, and the hallway is initially empty.

They give you a _diagram of the situation_ (your puzzle input), including locations of each amphipod (`A`, `B`, `C`, or `D`, each of which is occupying an otherwise open space), walls (`#`), and open space (`.`).

For example:

    #############
    #...........#
    ###B#C#B#D###
      #A#D#C#A#
      #########
    

The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted `A`\-`D` going left to right, like this:

    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #########
    

Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of _energy_ to move one step: Amber amphipods require `1` energy per step, Bronze amphipods require `10` energy, Copper amphipods require `100`, and Desert ones require `1000`. The amphipods would like you to find a way to organize the amphipods that requires the _least total energy_.

However, because they are timid and stubborn, the amphipods have some extra rules:

*   Amphipods will never _stop on the space immediately outside any room_. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)
*   Amphipods will never _move from the hallway into a room_ unless that room is their destination room _and_ that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)
*   Once an amphipod stops moving in the hallway, _it will stay in that spot until it can move into a room_. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)

In the above example, the amphipods can be organized using a minimum of _`12521`_ energy. One way to do this is shown below.

Starting configuration:

    #############
    #...........#
    ###B#C#B#D###
      #A#D#C#A#
      #########
    

One Bronze amphipod moves into the hallway, taking 4 steps and using `40` energy:

    #############
    #...B.......#
    ###B#C#.#D###
      #A#D#C#A#
      #########
    

The only Copper amphipod not in its side room moves there, taking 4 steps and using `400` energy:

    #############
    #...B.......#
    ###B#.#C#D###
      #A#D#C#A#
      #########
    

A Desert amphipod moves out of the way, taking 3 steps and using `3000` energy, and then the Bronze amphipod takes its place, taking 3 steps and using `30` energy:

    #############
    #.....D.....#
    ###B#.#C#D###
      #A#B#C#A#
      #########
    

The leftmost Bronze amphipod moves to its room using `40` energy:

    #############
    #.....D.....#
    ###.#B#C#D###
      #A#B#C#A#
      #########
    

Both amphipods in the rightmost room move into the hallway, using `2003` energy in total:

    #############
    #.....D.D.A.#
    ###.#B#C#.###
      #A#B#C#.#
      #########
    

Both Desert amphipods move into the rightmost room using `7000` energy:

    #############
    #.........A.#
    ###.#B#C#D###
      #A#B#C#D#
      #########
    

Finally, the last Amber amphipod moves into its room, using `8` energy:

    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #########
    

_What is the least energy required to organize the amphipods?_

Your puzzle answer was `12530`.


## Part 2

As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:

      #D#C#B#A#
      #D#B#A#C#
    

So, the above example now becomes:

    #############
    #...........#
    ###B#C#B#D###
      #D#C#B#A#
      #D#B#A#C#
      #A#D#C#A#
      #########
    

The amphipods still want to be organized into rooms similar to before:

    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #A#B#C#D#
      #A#B#C#D#
      #########
    

In this updated example, the least energy required to organize these amphipods is _`44169`_:

    #############
    #...........#
    ###B#C#B#D###
      #D#C#B#A#
      #D#B#A#C#
      #A#D#C#A#
      #########
    
    #############
    #..........D#
    ###B#C#B#.###
      #D#C#B#A#
      #D#B#A#C#
      #A#D#C#A#
      #########
    
    #############
    #A.........D#
    ###B#C#B#.###
      #D#C#B#.#
      #D#B#A#C#
      #A#D#C#A#
      #########
    
    #############
    #A........BD#
    ###B#C#.#.###
      #D#C#B#.#
      #D#B#A#C#
      #A#D#C#A#
      #########
    
    #############
    #A......B.BD#
    ###B#C#.#.###
      #D#C#.#.#
      #D#B#A#C#
      #A#D#C#A#
      #########
    
    #############
    #AA.....B.BD#
    ###B#C#.#.###
      #D#C#.#.#
      #D#B#.#C#
      #A#D#C#A#
      #########
    
    #############
    #AA.....B.BD#
    ###B#.#.#.###
      #D#C#.#.#
      #D#B#C#C#
      #A#D#C#A#
      #########
    
    #############
    #AA.....B.BD#
    ###B#.#.#.###
      #D#.#C#.#
      #D#B#C#C#
      #A#D#C#A#
      #########
    
    #############
    #AA...B.B.BD#
    ###B#.#.#.###
      #D#.#C#.#
      #D#.#C#C#
      #A#D#C#A#
      #########
    
    #############
    #AA.D.B.B.BD#
    ###B#.#.#.###
      #D#.#C#.#
      #D#.#C#C#
      #A#.#C#A#
      #########
    
    #############
    #AA.D...B.BD#
    ###B#.#.#.###
      #D#.#C#.#
      #D#.#C#C#
      #A#B#C#A#
      #########
    
    #############
    #AA.D.....BD#
    ###B#.#.#.###
      #D#.#C#.#
      #D#B#C#C#
      #A#B#C#A#
      #########
    
    #############
    #AA.D......D#
    ###B#.#.#.###
      #D#B#C#.#
      #D#B#C#C#
      #A#B#C#A#
      #########
    
    #############
    #AA.D......D#
    ###B#.#C#.###
      #D#B#C#.#
      #D#B#C#.#
      #A#B#C#A#
      #########
    
    #############
    #AA.D.....AD#
    ###B#.#C#.###
      #D#B#C#.#
      #D#B#C#.#
      #A#B#C#.#
      #########
    
    #############
    #AA.......AD#
    ###B#.#C#.###
      #D#B#C#.#
      #D#B#C#.#
      #A#B#C#D#
      #########
    
    #############
    #AA.......AD#
    ###.#B#C#.###
      #D#B#C#.#
      #D#B#C#.#
      #A#B#C#D#
      #########
    
    #############
    #AA.......AD#
    ###.#B#C#.###
      #.#B#C#.#
      #D#B#C#D#
      #A#B#C#D#
      #########
    
    #############
    #AA.D.....AD#
    ###.#B#C#.###
      #.#B#C#.#
      #.#B#C#D#
      #A#B#C#D#
      #########
    
    #############
    #A..D.....AD#
    ###.#B#C#.###
      #.#B#C#.#
      #A#B#C#D#
      #A#B#C#D#
      #########
    
    #############
    #...D.....AD#
    ###.#B#C#.###
      #A#B#C#.#
      #A#B#C#D#
      #A#B#C#D#
      #########
    
    #############
    #.........AD#
    ###.#B#C#.###
      #A#B#C#D#
      #A#B#C#D#
      #A#B#C#D#
      #########
    
    #############
    #..........D#
    ###A#B#C#.###
      #A#B#C#D#
      #A#B#C#D#
      #A#B#C#D#
      #########
    
    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #A#B#C#D#
      #A#B#C#D#
      #########
    

Using the initial configuration from the full diagram, _what is the least energy required to organize the amphipods?_

Your puzzle answer was `50492`.


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
