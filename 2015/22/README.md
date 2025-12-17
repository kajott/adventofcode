# [2015, Day 22: Wizard Simulator 20XX](https://adventofcode.com/2015/day/22)


## Solution Notes

This puzzle is about simulation of a rather complex ruleset, combined with a search algorithm. My approach is to have an queue of game states to explore, and for each state, process a single turn and generate the possible result states. The queue is sorted such that states with lower amount of mana spent are expanded first; as a result, the first visited state that represents a win for the player is the solution.

Due to the complexity, I did the puzzle in a non-golf version first. In the golf version, the whole state is represented as an 8-tuple of integers, with the following mapping:


| index | non-golf field     | description |
| ----- | ------------------ | ----------- |
| `[0]` | `mana_spent`       | amount of mana spent by the player so far |
| `[1]` | `boss_hp`          | remaining hit points of the boss |
| `[2]` | `player_hp`        | remaining hit points of the player |
| `[3]` | `mana`             | amount of mana left for the player |
| `[4]` | `turn`             | `0` = player's turn, `1` = boss's turn |
| `[5]` | `shield_timeout`   | number of turns left until the Shield spell wears out |
| `[6]` | `poison_timeout`   | number of turns left until the Poison spell wears out |
| `[7]` | `recharge_timeout` | number of turns left until the Recharge spell wears out |

Compared to part 1, part 2 is just a single additional line (and a few seconds of runtime).

* Part 1, Python: 530 bytes, ~1 s
* Part 2, Python: 547 bytes, ~5 s
