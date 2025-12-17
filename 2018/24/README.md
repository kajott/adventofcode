# 2018, Day 24: Immune System Simulator 20XX


## Solution Notes

This puzzle is superficially very similar to [day 15's](../15), except that it significantly less complex and requires less algorithm knowledge. In the end, all that needs to be done is write the rules down as code and let the simulation run. There are still some fine details that can easily be overlooked, and parsing the input file is quite laborious, but there's really nothing special about it.

Still, the complexity of the task description made me write a non-golf version first and shrink it down later, into one common implementation for both parts. Since I use lists instead of classes in golf, keeping track of the various fields in the group list can be a little frustrating. Here's the key (mainly for my own reference):

| index | non-golf field | description |
| ----- | -------------- | ----------- |
| `[0]` | `-initiative`  | initiative (negative because it's used as a sort key at one point) |
| `[1]` | `team`         | 0 = Infection, 1 = Immune System |
| `[2]` | `units`        | number of units in the group |
| `[3]` | `hp`           | unit hit points |
| `[4]` | `modifiers`    | dictionary of attack type score modifiers (value 0 = immune, 2 = weak) |
| `[5]` | `attack`       | attack type |
| `[6]` | `damage`       | how many damage an attack deals |
| `[7]` | `target`       | reference to the attack target group |
| `[8]` | `not targeted` | whether the group is available as an attack target |

Indices 7 and 8 are reset after every round of the battle.


* Parts 1+2, Python: 839 bytes, ~5 s
