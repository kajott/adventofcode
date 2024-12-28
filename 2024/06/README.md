# 2024, Day 6: Guard Gallivant

The Historians use their fancy [device](../04) again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year [1518](../../2018/05)! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single _guard_ is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

## Part 1

You start by making a map (your puzzle input) of the situation. For example:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...

The map shows the current position of the guard with `^` (to indicate the guard is currently facing _up_ from the perspective of the map). Any _obstructions_ - crates, desks, alchemical reactors, etc. - are shown as `#`.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

*   If there is something directly in front of you, turn right 90 degrees.
*   Otherwise, take a step forward.

Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

    ....#.....
    ....^....#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...

Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

    ....#.....
    ........>#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...

Reaching another obstacle (a spool of several _very_ long polymers), she turns right again and continues downward:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#......v.
    ........#.
    #.........
    ......#...

This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#v..

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. _Including the guard's starting position_, the positions visited by the guard before leaving the area are marked with an `X`:

    ....#.....
    ....XXXXX#
    ....X...X.
    ..#.X...X.
    ..XXXXX#X.
    ..X.X.X.X.
    .#XXXXXXX.
    .XXXXXXX#.
    #XXXXXXX..
    ......#X..

In this example, the guard will visit _`41`_ distinct positions on your map.

Predict the path of the guard. _How many distinct positions will the guard visit before leaving the mapped area?_

Your puzzle answer was `5409`.

## Part 2

While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and [record](../../2018/04) the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are _pretty sure_ that adding a single new obstruction _won't_ cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get _stuck in a loop_, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know _all_ of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only _`6`_ different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use `O` to mark the new obstruction, `|` to show a position where the guard moves up/down, `-` to show a position where the guard moves left/right, and `+` to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ....|..#|.
    ....|...|.
    .#.O^---+.
    ........#.
    #.........
    ......#...

Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ......O.#.
    #.........
    ......#...

Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    .+----+O#.
    #+----+...
    ......#...

Option four, put an alchemical retroencabulator near the bottom left corner:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ..|...|.#.
    #O+---+...
    ......#...

Option five, put the alchemical retroencabulator a bit to the right instead:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ....|.|.#.
    #..O+-+...
    ......#...

Option six, put a tank of sovereign glue right next to the tank of universal solvent:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    .+----++#.
    #+----++..
    ......#O..

It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are _`6`_ different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. _How many different positions could you choose for this obstruction?_

Your puzzle answer was `2022`.

## Solution Notes

Part 1 is a fun exercise in utilizing the good old playfield-as-dictionary-indexed-by-complex-numbers approach, this time with a weirdly arranged coordinate system to make the initial direction constant shorter.

For part 2, there are two challenges: First, getting the loop check conditions exactly right, which is a bit finicky; and second, reducing the search space so runtime is acceptable. My very first approach tried to put an obstacle at every point of the maze (which has 130x130 elements in my case), but that took more than half a minute to compute. A straightforward way to reduce the search space is to only put obstacles where the guard's normal path (from part 1) was. This is only good for a ~3x reduction, but it's better than nothing, and allows for solving both parts with little more code than what's needed part 2 alone.

* Part 1, Python: 193 bytes, <100 ms
* Part 2, Python: 318 bytes, ~25 s
* Parts 1+2, Python: 350 bytes, ~25 s
