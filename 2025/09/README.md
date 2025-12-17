# 2025, Day 9: Movie Theater


## Solution Notes

Part 1 is nothing of note, part 2 is really where the meat is. And what a hunk of meat indeed! My first approach was to actually paint the path into a grid (or rather a set of complex numbers), use a flood fill to fill the interior (with multiple different seed points, trying them until one does *not* spill outside of the map), and then check every possible box if it's completely filled. Coordinate compression (a technique I've [used before](../../2013/18)) turns the large values from the actual input into something more manageable. However, that's a lot of steps and rather ugly code, and it's sloooow - over 1 minute on a really fast machine. I completely discarded this approach, because it's also very much unsuitable for code golf.

Instead, a much more elegant approach is now used that doesn't even start to rasterize the path in any way, shape or form. It's basically the same "find maximum area" loop as in part 1, but with an extra condition: a box is only eligible if it doesn't intersect with the polygon. To check that, it is sufficient to check whether any horizontal or vertical line that make up the polygon are intersecting with the perimeter of the box. It's not required to overthink things: Establishing the boundary conditions can be extremely prone to off-by-one errors, particularily in cases where two parallel lines have a distance of only 1 unit, and also, it would be required to check if a box is inside the polygon at all, etc. ... But none of this matters, as the input is relatively benign. The only trap, if you want to call it that way, is a thin wide strip of negative space right in the middle of the (circular, by the way) figure.

The non-golf version runs in 2-3 seconds, but for some reason, CPython 3.13 (which is the version I've been using at the time of writing) is unreasonably slow when running the golf version, even though it's doing basically the same things. I actually spent 16 not strictly necessary bytes to bring runtime down from almost a minute to what I have now. (Remove the `if k<1:break` line and see for yourself.) I've yet to find an explanation for this performance regression, but in the meantime, I take solace in the fact that at least PyPy runs everything in less than a second.

* Part 1, Python: 135 bytes, <100 ms
* Part 2, Python: 343 bytes, ~25 s
