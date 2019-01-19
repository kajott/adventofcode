# 2015, Day 22: Wizard Simulator 20XX

Little Henry Case decides that defeating bosses with [swords and stuff](21) is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

## Part 1

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below `0` hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do _magic damage_, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below `1`, it becomes `1` instead - that is, the boss' attacks always deal at least `1` damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost _mana_; you start with _500_ mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

*   _Magic Missile_ costs `53` mana. It instantly does `4` damage.
*   _Drain_ costs `73` mana. It instantly does `2` damage and heals you for `2` hit points.
*   _Shield_ costs `113` mana. It starts an _effect_ that lasts for `6` turns. While it is active, your armor is increased by `7`.
*   _Poison_ costs `173` mana. It starts an _effect_ that lasts for `6` turns. At the start of each turn while it is active, it deals the boss `3` damage.
*   _Recharge_ costs `229` mana. It starts an _effect_ that lasts for `5` turns. At the start of each turn while it is active, it gives you `101` new mana.

_Effects_ all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has `10` hit points and `250` mana, and that the boss has `13` hit points and `8` damage:

    -- Player turn --
    - Player has 10 hit points, 0 armor, 250 mana
    - Boss has 13 hit points
    Player casts Poison.
    
    -- Boss turn --
    - Player has 10 hit points, 0 armor, 77 mana
    - Boss has 13 hit points
    Poison deals 3 damage; its timer is now 5.
    Boss attacks for 8 damage.
    
    -- Player turn --
    - Player has 2 hit points, 0 armor, 77 mana
    - Boss has 10 hit points
    Poison deals 3 damage; its timer is now 4.
    Player casts Magic Missile, dealing 4 damage.
    
    -- Boss turn --
    - Player has 2 hit points, 0 armor, 24 mana
    - Boss has 3 hit points
    Poison deals 3 damage. This kills the boss, and the player wins.
    

Now, suppose the same initial conditions, except that the boss has `14` hit points instead:

    -- Player turn --
    - Player has 10 hit points, 0 armor, 250 mana
    - Boss has 14 hit points
    Player casts Recharge.
    
    -- Boss turn --
    - Player has 10 hit points, 0 armor, 21 mana
    - Boss has 14 hit points
    Recharge provides 101 mana; its timer is now 4.
    Boss attacks for 8 damage!
    
    -- Player turn --
    - Player has 2 hit points, 0 armor, 122 mana
    - Boss has 14 hit points
    Recharge provides 101 mana; its timer is now 3.
    Player casts Shield, increasing armor by 7.
    
    -- Boss turn --
    - Player has 2 hit points, 7 armor, 110 mana
    - Boss has 14 hit points
    Shield's timer is now 5.
    Recharge provides 101 mana; its timer is now 2.
    Boss attacks for 8 - 7 = 1 damage!
    
    -- Player turn --
    - Player has 1 hit point, 7 armor, 211 mana
    - Boss has 14 hit points
    Shield's timer is now 4.
    Recharge provides 101 mana; its timer is now 1.
    Player casts Drain, dealing 2 damage, and healing 2 hit points.
    
    -- Boss turn --
    - Player has 3 hit points, 7 armor, 239 mana
    - Boss has 12 hit points
    Shield's timer is now 3.
    Recharge provides 101 mana; its timer is now 0.
    Recharge wears off.
    Boss attacks for 8 - 7 = 1 damage!
    
    -- Player turn --
    - Player has 2 hit points, 7 armor, 340 mana
    - Boss has 12 hit points
    Shield's timer is now 2.
    Player casts Poison.
    
    -- Boss turn --
    - Player has 2 hit points, 7 armor, 167 mana
    - Boss has 12 hit points
    Shield's timer is now 1.
    Poison deals 3 damage; its timer is now 5.
    Boss attacks for 8 - 7 = 1 damage!
    
    -- Player turn --
    - Player has 1 hit point, 7 armor, 167 mana
    - Boss has 9 hit points
    Shield's timer is now 0.
    Shield wears off, decreasing armor by 7.
    Poison deals 3 damage; its timer is now 4.
    Player casts Magic Missile, dealing 4 damage.
    
    -- Boss turn --
    - Player has 1 hit point, 0 armor, 114 mana
    - Boss has 2 hit points
    Poison deals 3 damage. This kills the boss, and the player wins.
    

You start with _50 hit points_ and _500 mana points_. The boss's actual stats are in your puzzle input. What is the _least amount of mana_ you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)

Your puzzle answer was `953`.

## Part 2

On the next run through the game, you increase the difficulty to _hard_.

At the start of each _player turn_ (before any other effects apply), you lose `1` hit point. If this brings you to or below `0` hit points, you lose.

With the same starting stats for you and the boss, what is the _least amount of mana_ you can spend and still win the fight?

Your puzzle answer was `1289`.


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
