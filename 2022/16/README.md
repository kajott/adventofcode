# 2022, Day 16: Proboscidea Volcanium

The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have _30 minutes_ before the volcano erupts, so you don't have time to go back out the way you came in.

## Part 1

You scan the cave for other options and discover a network of pipes and pressure-release _valves_. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's _flow rate_ if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled `AA`. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

    Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    Valve BB has flow rate=13; tunnels lead to valves CC, AA
    Valve CC has flow rate=2; tunnels lead to valves DD, BB
    Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
    Valve EE has flow rate=3; tunnels lead to valves FF, DD
    Valve FF has flow rate=0; tunnels lead to valves EE, GG
    Valve GG has flow rate=0; tunnels lead to valves FF, HH
    Valve HH has flow rate=22; tunnel leads to valve GG
    Valve II has flow rate=0; tunnels lead to valves AA, JJ
    Valve JJ has flow rate=21; tunnel leads to valve II
    

All of the valves begin _closed_. You start at valve `AA`, but it must be damaged or jammed or something: its flow rate is `0`, so there's no point in opening it. However, you could spend one minute moving to valve `BB` and another minute opening it; doing so would release pressure during the remaining _28 minutes_ at a flow rate of `13`, a total eventual pressure release of `28 * 13 = `_`364`_. Then, you could spend your third minute moving to valve `CC` and your fourth minute opening it, providing an additional _26 minutes_ of eventual pressure release at a flow rate of `2`, or _`52`_ total pressure released by valve `CC`.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

    == Minute 1 ==
    No valves are open.
    You move to valve DD.
    
    == Minute 2 ==
    No valves are open.
    You open valve DD.
    
    == Minute 3 ==
    Valve DD is open, releasing 20 pressure.
    You move to valve CC.
    
    == Minute 4 ==
    Valve DD is open, releasing 20 pressure.
    You move to valve BB.
    
    == Minute 5 ==
    Valve DD is open, releasing 20 pressure.
    You open valve BB.
    
    == Minute 6 ==
    Valves BB and DD are open, releasing 33 pressure.
    You move to valve AA.
    
    == Minute 7 ==
    Valves BB and DD are open, releasing 33 pressure.
    You move to valve II.
    
    == Minute 8 ==
    Valves BB and DD are open, releasing 33 pressure.
    You move to valve JJ.
    
    == Minute 9 ==
    Valves BB and DD are open, releasing 33 pressure.
    You open valve JJ.
    
    == Minute 10 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve II.
    
    == Minute 11 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve AA.
    
    == Minute 12 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve DD.
    
    == Minute 13 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve EE.
    
    == Minute 14 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve FF.
    
    == Minute 15 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve GG.
    
    == Minute 16 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You move to valve HH.
    
    == Minute 17 ==
    Valves BB, DD, and JJ are open, releasing 54 pressure.
    You open valve HH.
    
    == Minute 18 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You move to valve GG.
    
    == Minute 19 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You move to valve FF.
    
    == Minute 20 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You move to valve EE.
    
    == Minute 21 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You open valve EE.
    
    == Minute 22 ==
    Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
    You move to valve DD.
    
    == Minute 23 ==
    Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
    You move to valve CC.
    
    == Minute 24 ==
    Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
    You open valve CC.
    
    == Minute 25 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    
    == Minute 26 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    
    == Minute 27 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    
    == Minute 28 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    
    == Minute 29 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    
    == Minute 30 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    

This approach lets you release the most pressure possible in 30 minutes with this valve layout, _`1651`_.

Work out the steps to release the most pressure in 30 minutes. _What is the most pressure you can release?_

Your puzzle answer was `1906`.

## Part 2

You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?

It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only _26 minutes_ to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)

In the example above, you could teach the elephant to help you as follows:

    == Minute 1 ==
    No valves are open.
    You move to valve II.
    The elephant moves to valve DD.
    
    == Minute 2 ==
    No valves are open.
    You move to valve JJ.
    The elephant opens valve DD.
    
    == Minute 3 ==
    Valve DD is open, releasing 20 pressure.
    You open valve JJ.
    The elephant moves to valve EE.
    
    == Minute 4 ==
    Valves DD and JJ are open, releasing 41 pressure.
    You move to valve II.
    The elephant moves to valve FF.
    
    == Minute 5 ==
    Valves DD and JJ are open, releasing 41 pressure.
    You move to valve AA.
    The elephant moves to valve GG.
    
    == Minute 6 ==
    Valves DD and JJ are open, releasing 41 pressure.
    You move to valve BB.
    The elephant moves to valve HH.
    
    == Minute 7 ==
    Valves DD and JJ are open, releasing 41 pressure.
    You open valve BB.
    The elephant opens valve HH.
    
    == Minute 8 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You move to valve CC.
    The elephant moves to valve GG.
    
    == Minute 9 ==
    Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
    You open valve CC.
    The elephant moves to valve FF.
    
    == Minute 10 ==
    Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
    The elephant moves to valve EE.
    
    == Minute 11 ==
    Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
    The elephant opens valve EE.
    
    (At this point, all valves are open.)
    
    == Minute 12 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    
    ...
    
    == Minute 20 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    
    ...
    
    == Minute 26 ==
    Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
    

With the elephant helping, after 26 minutes, the best you could do would release a total of _`1707`_ pressure.

_With you and an elephant working together for 26 minutes, what is the most pressure you could release?_

Your puzzle answer was `2548`.

## Solution Notes

This is a tough one. It's essentially a graph searching puzzle where every possible move is a node, and can be tackled with Dijkstra's algorithm or DFS with memoization as usual; however, there are quite a few tiny details to get exactly right, lest the whole thing blows up in terms of computation power and memory usage.

For example, I included the projected flow rate into my DFS state - a bad idea. Later on, I temporarily switched to Dijkstra (because I thought that DFS is unviable due to my earlier failure with it), which worked beautifully for part 1, but for part 2, it generated wrong results on the example data and ran forever on the actual input. The reason: I included the time in my scoring function, whereas it should be part of the state instead. Computation still took 10 minutes though, and I didn't bother to clean up and golf that code as a result.

After getting a few hints from other contestants, I switched back to DFS with the "proper" set of states, and this does the trick indeed - it's relatively slow, but it's quite lean and it works.

For part 2, there is a pretty neat trick that helps to drastically reduce the complexity (in terms of code size, not necessarily runtime complexity): Instead of simulating both players at the same time, they can be serialized. Once player 1's time runs out, player 2 gets another 26 minutes of time to close the remaining valves. This enables a relatively compact DFS+memoization-based implementation.

It's still very slow though; a useful optimization is to run a BFS first to compute a distance matrix between all valves, like in [2019/18](../../2019/18). The main DFS can then use this data to perform movement and valve opening as one atomic operation, thus severely cutting down the number of graph nodes to search.

* Part 1, Python (DFS only): 340 bytes, ~2.5 s
* Part 2, Python (DFS only): 395 bytes, ~1.5 min
* Part 2, Python (BFS+DFS): 507 bytes, ~20 s
