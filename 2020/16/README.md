# 2020, Day 16: Ticket Translation


## Solution Notes

A highly complex puzzle, not because it contains any real head-scratchers, but because it requires some serious data juggling, starting with the parser already.

Part 1 can be solved with lots of shortcuts, which I made good use of in my golf implementation.

Part 2 is constructed in a way that ruling out impossible field associations by checking all constraints is *not* sufficient: Only one of the fields will be uniquely identified, the others must be reconstructed by resolving (and subsequently ignoring) the unique identifications first.

* Part 1, Python: 204 bytes, <100 ms
* Part 2, Python: 528 bytes, <100 ms
