# 2025, Day 5: Cafeteria

As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are _fresh_ and which are _spoiled_. When you ask how it works, they give you a copy of their database (your puzzle input).

## Part 1

The database operates on _ingredient IDs_. It consists of a list of _fresh ingredient ID ranges_, a blank line, and a list of _available ingredient IDs_. For example:

    3-5
    10-14
    16-20
    12-18
    
    1
    5
    8
    11
    17
    32
    

The fresh ID ranges are _inclusive_: the range `3-5` means that ingredient IDs `3`, `4`, and `5` are all _fresh_. The ranges can also _overlap_; an ingredient ID is fresh if it is in _any_ range.

The Elves are trying to determine which of the _available ingredient IDs_ are _fresh_. In this example, this is done as follows:

*   Ingredient ID `1` is spoiled because it does not fall into any range.
*   Ingredient ID `5` is _fresh_ because it falls into range `3-5`.
*   Ingredient ID `8` is spoiled.
*   Ingredient ID `11` is _fresh_ because it falls into range `10-14`.
*   Ingredient ID `17` is _fresh_ because it falls into range `16-20` as well as range `12-18`.
*   Ingredient ID `32` is spoiled.

So, in this example, _`3`_ of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. _How many of the available ingredient IDs are fresh?_

Your puzzle answer was `652`.

## Part 2

The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know _all_ of the IDs that the _fresh ingredient ID ranges_ consider to be _fresh_. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

    3-5
    10-14
    16-20
    12-18
    

The ingredient IDs that these ranges consider to be fresh are `3`, `4`, `5`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, and `20`. So, in this example, the fresh ingredient ID ranges consider a total of _`14`_ ingredient IDs to be fresh.

Process the database file again. _How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?_

Your puzzle answer was `341753674214273`.


## Solution Notes

Part 1 is a trivial starter with the biggest hurdle (if one could call it that way) being the parsing process of the two-part input.

The obvious way to implement part 2 is what I would call a "union algorithm on sets of ranges" (no idea if there is a proper name for that): Have a sorted list of ranges, and for every new range, compute its union with the existing list. This sounds simple, but getting all the conditions and special cases right (like a range spanning multiple existing ranges) can be a major pain.

The usual shortcuts are non-starters too: The numbers are too huge to use actual sets of distinct numbers, and the ranges are of course overlapping and nesting like crazy.

I eventually came up with a more elegant solution that doesn't induce any headaches. First off, I convert the closed ranges into Python-style half-open intervals; that's the proper representation anyway, and it's crucially important in this case. Then, I don't keep a list of _ranges_, but only of _edges_, i.e. range start or end positions. Each edge is tagged with the information whether it's range start (+1) or range end (-1). This edge list can then be sorted and the tags can be integrated, i.e. summed up. Thus, for every edge it's known how many intervals cover the range between the previous edge and the current one. If that number is nonzero, the range can be added to the total size.

This algorithm can also be turned into a proper range set union operation by looking only at the edges where the nesting level becomes nonzero or goes down to zero again. That's not needed for the task at hand though.

* Part 1, Python: 136 bytes, <100 ms
* Part 2, Python: 152 bytes, <100 ms
