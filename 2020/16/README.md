# [2020, Day 16: Ticket Translation](https://adventofcode.com/2020/day/16)

The input consists of two parts. First, the the definitions of (typically) 20 **fields** with names normally found on train tickets ("train", "route", "seat", "departure time" etc.). For each field, two 2-to-3-digit numerical ranges are defined. The ranges for different fields overlap considerably.
Second, the input contains the data of (typically) 260 tickets, as a lists of 2-to-3-digit numbers, one item per field. The order of the fields is unknown, but identical on each ticket. One of the tickets is marked as "your ticket".

**Part 1** asks to identify invalid tickets by checking for numbers that don't match any of the field ranges.

**Part 2** asks to reconstruct the field order and decode all fields of "your ticket". The invalid tickets identified in part 1 are ignored.


## Solution Notes

A highly complex puzzle, not because it contains any real head-scratchers, but because it requires some serious data juggling, starting with the parser already.

Part 1 can be solved with lots of shortcuts, which I made good use of in my golf implementation.

Part 2 is constructed in a way that ruling out impossible field associations by checking all constraints is *not* sufficient: Only one of the fields will be uniquely identified, the others must be reconstructed by resolving (and subsequently ignoring) the unique identifications first.

* Part 1, Python: 204 bytes, <100 ms
* Part 2, Python: 528 bytes, <100 ms
