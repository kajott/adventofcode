# 2024, Day 21: Keypad Conundrum

As you teleport onto Santa's [Reindeer-class starship](../../2019/25), The Historians begin to panic: someone from their search party is _missing_. A quick life-form scan by the ship's computer reveals that when the missing Historian teleported, he arrived in another part of the ship.

The door to that area is locked, but the computer can't open it; it can only be opened by _physically typing_ the door codes (your puzzle input) on the numeric keypad on the door.

## Part 1

The numeric keypad has four rows of buttons: `789`, `456`, `123`, and finally an empty gap followed by `0A`. Visually, they are arranged like this:

    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+

Unfortunately, the area outside the door is currently _depressurized_ and nobody can go near the door. A robot needs to be sent instead.

The robot has no problem navigating the ship and finding the numeric keypad, but it's not designed for button pushing: it can't be told to push a specific button directly. Instead, it has a robotic arm that can be controlled remotely via a _directional keypad_.

The directional keypad has two rows of buttons: a gap / `^` (up) / `A` (activate) on the first row and `<` (left) / `v` (down) / `>` (right) on the second row. Visually, they are arranged like this:

        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+

When the robot arrives at the numeric keypad, its robotic arm is pointed at the `A` button in the bottom right corner. After that, this directional keypad remote control must be used to maneuver the robotic arm: the up / down / left / right buttons cause it to move its arm one button in that direction, and the `A` button causes the robot to briefly move forward, pressing the button being aimed at by the robotic arm.

For example, to make the robot type `029A` on the numeric keypad, one sequence of inputs on the directional keypad you could use is:

*   `<` to move the arm from `A` (its initial position) to `0`.
*   `A` to push the `0` button.
*   `^A` to move the arm to the `2` button and push it.
*   `>^^A` to move the arm to the `9` button and push it.
*   `vvvA` to move the arm to the `A` button and push it.

In total, there are three shortest possible sequences of button presses on this directional keypad that would cause the robot to type `029A`: `<A^A>^^AvvvA`, `<A^A^>^AvvvA`, and `<A^A^^>AvvvA`.

Unfortunately, the area containing this directional keypad remote control is currently experiencing _high levels of radiation_ and nobody can go near it. A robot needs to be sent instead.

When the robot arrives at the directional keypad, its robot arm is pointed at the `A` button in the upper right corner. After that, a _second, different_ directional keypad remote control is used to control this robot (in the same way as the first robot, except that this one is typing on a directional keypad instead of a numeric keypad).

There are multiple shortest possible sequences of directional keypad button presses that would cause this robot to tell the first robot to type `029A` on the door. One such sequence is `v<<A>>^A<A>AvA<^AA>A<vAAA>^A`.

Unfortunately, the area containing this second directional keypad remote control is currently _`-40` degrees_! Another robot will need to be sent to type on that directional keypad, too.

There are many shortest possible sequences of directional keypad button presses that would cause this robot to tell the second robot to tell the first robot to eventually type `029A` on the door. One such sequence is `<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A`.

Unfortunately, the area containing this third directional keypad remote control is currently _full of Historians_, so no robots can find a clear path there. Instead, _you_ will have to type this sequence yourself.

Were you to choose this sequence of button presses, here are all of the buttons that would be pressed on your directional keypad, the two robots' directional keypads, and the numeric keypad:

    <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
    v<<A>>^A<A>AvA<^AA>A<vAAA>^A
    <A^A>^^AvvvA
    029A

In summary, there are the following keypads:

*   One directional keypad that _you_ are using.
*   Two directional keypads that _robots_ are using.
*   One numeric keypad (on a door) that a _robot_ is using.

It is important to remember that these robots are not designed for button pushing. In particular, if a robot arm is ever aimed at a _gap_ where no button is present on the keypad, even for an instant, the robot will _panic_ unrecoverably. So, don't do that. All robots will initially aim at the keypad's `A` key, wherever it is.

To unlock the door, _five_ codes will need to be typed on its numeric keypad. For example:

    029A
    980A
    179A
    456A
    379A

For each of these, here is a shortest sequence of button presses you could type to cause the desired code to be typed on the numeric keypad:

    029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
    980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
    179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
    456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
    379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

The Historians are getting nervous; the ship computer doesn't remember whether the missing Historian is trapped in the area containing a _giant electromagnet_ or _molten lava_. You'll need to make sure that for each of the five codes, you find the _shortest sequence_ of button presses necessary.

The _complexity_ of a single code (like `029A`) is equal to the result of multiplying these two values:

*   The _length of the shortest sequence_ of button presses you need to type on your directional keypad in order to cause the code to be typed on the numeric keypad; for `029A`, this would be `68`.
*   The _numeric part of the code_ (ignoring leading zeroes); for `029A`, this would be `29`.

In the above example, complexity of the five codes can be found by calculating `68 * 29`, `60 * 980`, `68 * 179`, `64 * 456`, and `64 * 379`. Adding these together produces _`126384`_.

Find the fewest number of button presses you'll need to perform in order to cause the robot in front of the door to type each code. _What is the sum of the complexities of the five codes on your list?_

Your puzzle answer was `105458`.

## Part 2

Just as the missing Historian is released, The Historians realize that a _second_ member of their search party has also been missing this entire time!

A quick life-form scan reveals the Historian is also trapped in a locked area of the ship. Due to a variety of hazards, robots are once again dispatched, forming another chain of remote control keypads managing robotic-arm-wielding robots.

This time, many more robots are involved. In summary, there are the following keypads:

*   One directional keypad that _you_ are using.
*   _25_ directional keypads that _robots_ are using.
*   One numeric keypad (on a door) that a _robot_ is using.

The keypads form a chain, just like before: your directional keypad controls a robot which is typing on a directional keypad which controls a robot which is typing on a directional keypad... and so on, ending with the robot which is typing on the numeric keypad.

The door codes are the same this time around; only the number of robots and directional keypads has changed.

Find the fewest number of button presses you'll need to perform in order to cause the robot in front of the door to type each code. _What is the sum of the complexities of the five codes on your list?_

Your puzzle answer was `129551515895690`.

## Solution Notes

This puzzle has a lot of pitfalls that make it extra hard to solve (I took several hours and one full rewrite), but at its core, it's just a recursive search for the path through the keypad that enters a certain sequence with minimal input length on the _next_ keypad. Memoization is required for part 2, lest the search tree becomes too deep to be feasible without it, but that's in fact the only required change once the rest of the algorithm is sound. It's only about 50 lines of non-golf Python, but unfortunately it doesn't golf too well, coming in at about 500 bytes.

* Part 1, Python: 478 bytes, <100 ms
* Part 2, Python: 510 bytes, <100 ms
