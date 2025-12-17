# 2025, Day 5: Cafeteria


## Solution Notes

Part 1 is a trivial starter with the biggest hurdle (if one could call it that way) being the parsing process of the two-part input.

The obvious way to implement part 2 is what I would call a "union algorithm on sets of ranges" (no idea if there is a proper name for that): Have a sorted list of ranges, and for every new range, compute its union with the existing list. This sounds simple, but getting all the conditions and special cases right (like a range spanning multiple existing ranges) can be a major pain.

The usual shortcuts are non-starters too: The numbers are too huge to use actual sets of distinct numbers, and the ranges are of course overlapping and nesting like crazy.

I eventually came up with a more elegant solution that doesn't induce any headaches. First off, I convert the closed ranges into Python-style half-open intervals; that's the proper representation anyway, and it's crucially important in this case. Then, I don't keep a list of _ranges_, but only of _edges_, i.e. range start or end positions. Each edge is tagged with the information whether it's range start (+1) or range end (-1). This edge list can then be sorted and the tags can be integrated, i.e. summed up. Thus, for every edge it's known how many intervals cover the range between the previous edge and the current one. If that number is nonzero, the range can be added to the total size.

This algorithm can also be turned into a proper range set union operation by looking only at the edges where the nesting level becomes nonzero or goes down to zero again. That's not needed for the task at hand though.

* Part 1, Python: 136 bytes, <100 ms
* Part 2, Python: 152 bytes, <100 ms
