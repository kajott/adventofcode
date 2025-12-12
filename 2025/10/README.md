# 2025, Day 10: Factory

Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.

## Part 1

The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a [Shiba Inu](https://en.wikipedia.org/wiki/Shiba_Inu). All that remains of the manual are some indicator light diagrams, button wiring schematics, and [joltage](3) requirements for each machine.

For example:

    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    

The manual describes one machine per line. Each line contains a single indicator light diagram in `[`square brackets`]`, one or more button wiring schematics in `(`parentheses`)`, and joltage requirements in `{`curly braces`}`.

To start a machine, its _indicator lights_ must match those shown in the diagram, where `.` means _off_ and `#` means _on_. The machine has the number of indicator lights shown, but its indicator lights are all _initially off_.

So, an indicator light diagram like `[.##.]` means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.

You can _toggle_ the state of indicator lights by pushing any of the listed _buttons_. Each button lists which indicator lights it toggles, where `0` means the first light, `1` means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).

So, a button wiring schematic like `(0,3,4)` means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were `[#.....]`, pushing the button would change them to be `[...##.]` instead.

Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.

You can push each button as many times as you like. However, to save on time, you will need to determine the _fewest total presses_ required to correctly configure all indicator lights for all machines in your list.

There are a few ways to correctly configure the first machine:

    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

*   You could press the first three buttons once each, a total of `3` button presses.
*   You could press `(1,3)` once, `(2,3)` once, and `(0,1)` twice, a total of `4` button presses.
*   You could press all of the buttons except `(1,3)` once each, a total of `5` button presses.

However, the fewest button presses required is _`2`_. One way to do this is by pressing the last two buttons (`(0,2)` and `(0,1)`) once each.

The second machine can be configured with as few as _`3`_ button presses:

    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}

One way to achieve this is by pressing the last three buttons (`(0,4)`, `(0,1,2)`, and `(1,2,3,4)`) once each.

The third machine has a total of six indicator lights that need to be configured correctly:

    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

The fewest presses required to correctly configure it is _`2`_; one way to do this is by pressing buttons `(0,3,4)` and `(0,1,2,4,5)` once each.

So, the fewest button presses required to correctly configure the indicator lights on all of the machines is `2` + `3` + `2` = _`7`_.

Analyze each machine's indicator light diagram and button wiring schematics. _What is the fewest button presses required to correctly configure the indicator lights on all of the machines?_

Your puzzle answer was `441`.

## Part 2

All of the machines are starting to come online! Now, it's time to worry about the joltage requirements.

Each machine needs to be configured to _exactly the specified joltage levels_ to function properly. Below the buttons on each machine is a big lever that you can use to switch the buttons from configuring the indicator lights to increasing the joltage levels. (Ignore the indicator light diagrams.)

The machines each have a set of _numeric counters_ tracking its joltage levels, one counter per joltage requirement. The counters are all _initially set to zero_.

So, joltage requirements like `{3,5,4,7}` mean that the machine has four counters which are initially `0` and that the goal is to simultaneously configure the first counter to be `3`, the second counter to be `5`, the third to be `4`, and the fourth to be `7`.

The button wiring schematics are still relevant: in this new joltage configuration mode, each button now indicates which counters it affects, where `0` means the first counter, `1` means the second counter, and so on. When you push a button, each listed counter is _increased by `1`_.

So, a button wiring schematic like `(1,3)` means that each time you push that button, the second and fourth counters would each increase by `1`. If the current joltage levels were `{0,1,2,3}`, pushing the button would change them to be `{0,2,2,4}`.

You can push each button as many times as you like. However, your finger is getting sore from all the button pushing, and so you will need to determine the _fewest total presses_ required to correctly configure each machine's joltage level counters to match the specified joltage requirements.

Consider again the example from before:

    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    

Configuring the first machine's counters requires a minimum of _`10`_ button presses. One way to do this is by pressing `(3)` once, `(1,3)` three times, `(2,3)` three times, `(0,2)` once, and `(0,1)` twice.

Configuring the second machine's counters requires a minimum of _`12`_ button presses. One way to do this is by pressing `(0,2,3,4)` twice, `(2,3)` five times, and `(0,1,2)` five times.

Configuring the third machine's counters requires a minimum of _`11`_ button presses. One way to do this is by pressing `(0,1,2,3,4)` five times, `(0,1,2,4,5)` five times, and `(1,2)` once.

So, the fewest button presses required to correctly configure the joltage level counters on all of the machines is `10` + `12` + `11` = _`33`_.

Analyze each machine's joltage requirements and button wiring schematics. _What is the fewest button presses required to correctly configure the joltage level counters on all of the machines?_

Your puzzle answer was `18559`.


## Solution Notes

The two parts are completely different from each other.

Part 1 is an easy starter that calls for a bit of XOR magic, based on the realization that it never makes sense to push any of the buttons twice, as the results would cancel out. Brute-force checking of all combinations is a perfectly viable solution there.

This is not the case for part 2. I tried DFS with memoization, but that lead nowhere. Some people had success with clever searching approaches (I've seen a Dijkstra variant even), but those are excruciatingly slow too. No, there's exactly one proper way to solve this, and it's algebra.

Each line in the input describes a linear system of integers; most are underconstrained, others are overconstrained, and a few are perfectly square. Solving such a system purely in integers is technically an NP-complete problem; it's not surprising that most participants used a ready-made third-party solver like Z3 or SciPy's `optimize` sub-package. Admittedly, I did the same out of frustration, and it's indeed remarkable how compact and fast a solution based on that approach can be.

But it still feels like cheating. So I took another three(!) nights to solve the task "properly": a modified Gauss-Jordan algorithm that works on integers transforms the problem matrix into a (probably scaled) identity matrix with 0 to 3 extra columns tacked on at the right side. To resolve those, a simplex search could be used (which is likely what the solver libraries do), or a well-constrained brute force search. Since it's only up to 3 variables, and the ranges can be limited by computing the maximum amount of "button presses" until any of the "joltages" is exceeded, the resulting performance is absolutely fine.
The code size, however, isn't. It's almost certain that there are algorithmic optimizations with which I could get the size down and probably even break the kilobyte barrier, but since I already invested an inordinate amount of time on this entire endeavour, I didn't poke any further and just edited my non-golf approach down.

* Part 1, Python: 303 bytes, ~400 ms
* Part 2, Python (using SciPy): 240 bytes, ~600 ms
* Part 2, Python (handwritten algebra): 1046 bytes, ~1.5 s
