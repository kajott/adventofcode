# 2020, Day 11: Seating System

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

## Part 1

The seat layout fits neatly on a grid. Each position is either floor (`.`), an empty seat (`L`), or an occupied seat (`#`). For example, the initial seat layout might look like this:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the _number of occupied seats_ adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

*   If a seat is _empty_ (`L`) and there are _no_ occupied seats adjacent to it, the seat becomes _occupied_.
*   If a seat is _occupied_ (`#`) and _four or more_ seats adjacent to it are also occupied, the seat becomes _empty_.
*   Otherwise, the seat's state does not change.

Floor (`.`) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##
    

After a second round, the seats with four or more occupied adjacent seats become empty again:

    #.LL.L#.##
    #LLLLLL.L#
    L.L.L..L..
    #LLL.LL.L#
    #.LL.LL.LL
    #.LLLL#.##
    ..L.L.....
    #LLLLLLLL#
    #.LLLLLL.L
    #.#LLLL.##
    

This process continues for three more rounds:

    #.##.L#.##
    #L###LL.L#
    L.#.#..#..
    #L##.##.L#
    #.##.LL.LL
    #.###L#.##
    ..#.#.....
    #L######L#
    #.LL###L.L
    #.#L###.##
    

    #.#L.L#.##
    #LLL#LL.L#
    L.L.L..#..
    #LLL.##.L#
    #.LL.LL.LL
    #.LL#L#.##
    ..L.L.....
    #L#LLLL#L#
    #.LLLLLL.L
    #.#L#L#.##
    

    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##
    

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count _`37`_ occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. _How many seats end up occupied?_

Your puzzle answer was `2303`.

## Part 2

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about _the first seat they can see_ in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the _first seat_ in each of those eight directions. For example, the empty seat below would see _eight_ occupied seats:

    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....
    

The leftmost empty seat below would only see _one_ empty seat, but cannot see any of the occupied ones:

    .............
    .L.L.#.#.#.#.
    .............
    

The empty seat below would see _no_ occupied seats:

    .##.##.
    #.#.#.#
    ##...##
    ...L...
    ##...##
    #.#.#.#
    .##.##.
    

Also, people seem to be more tolerant than you expected: it now takes _five or more_ visible occupied seats for an occupied seat to become empty (rather than _four or more_ from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##
    

    #.LL.LL.L#
    #LLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLL#
    #.LLLLLL.L
    #.LLLLL.L#
    

    #.L#.##.L#
    #L#####.LL
    L.#.#..#..
    ##L#.##.##
    #.##.#L.##
    #.#####.#L
    ..#.#.....
    LLL####LL#
    #.L#####.L
    #.L####.L#
    

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##LL.LL.L#
    L.LL.LL.L#
    #.LLLLL.LL
    ..L.L.....
    LLLLLLLLL#
    #.LLLLL#.L
    #.L#LL#.L#
    

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##L#.#L.L#
    L.L#.#L.L#
    #.L####.LL
    ..#.#.....
    LLL###LLL#
    #.LLLLL#.L
    #.L#LL#.L#
    

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##L#.#L.L#
    L.L#.LL.L#
    #.LLLL#.LL
    ..#.L.....
    LLL###LLL#
    #.LLLLL#.L
    #.L#LL#.L#
    

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count _`26`_ occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, _how many seats end up occupied?_

Your puzzle answer was `2057`.


## Solution Notes

A straightforward 2D cellular automaton simulation, albeit with three possible states.

I tried two different implementations for part 1 here: first the "classical" way with a two-dimensional array, and then using the good old "dictionary indexed by complex number" trick. The latter is slower, but considerably smaller, and it forms a formidable base for part 2: The only difference is that except looking for the immediate neighbors, there's a little scan routine that increments the position by the delta until a seat is found. Border handling is quite costly though, but that would be the case either way.

Out of curiosity, I also implemented a (non-golf) C version to see just how fast it is, and sure enough, it's 20x as fast as the Python version, **including** compilation. (Without compilation, it's 100x.)

* Part 1, Python (with 2D arrays): 347 bytes, ~1.5 s
* Part 1, Python (with dictionaries): 269 bytes, ~2.5 s
* Part 2, Python: 373 bytes, ~3 s
* Part 2, C: 2168 bytes, ~150 ms
