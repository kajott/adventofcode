# 2021, Day 19: Beacon Scanner


## Solution Notes

For this puzzle, it's very hard to come up with even an initial idea how to approach the problem. The orientations are clear: that's just vector math with one of 48 (not just 24 as stated in the description!) nearly-trivial rotation matrices. But how to compute the offsets when merging two point sets ("probes")? There might be some clever way, but I didn't find one; in the end, I just used a brute-force comparison of every point ("beacon") in one set ("probe") with every _rotated_ point of the other set. If the resulting delta vector appears at least 12 times, it must be the solution and the sets can be merged. That merge operation is carried out repeatedly until there's only one set left.

The golf version is again a near-literal transcript of the non-golf version; the only interesting part is encoding the rotation matrices. A true 3x3 matrix isn't needed, as we're only dealing with _shuffles_ of the original components (of which there a 6 different combinations) and _sign flips_ for each of the three components; that makes 6x8 = 48 combinations in total. For the golf version, I strictly decomposed the _shuffle_ part (`o` = "order" vector) and the _sign flip_ part (`m` = "multiply" vector). The construction of these two arrays is perhaps the only real fun thing in this whole puzzle :)

* Part 1, Python: 532 bytes, ~30 s
* Part 2, Python: 610 bytes, ~30 s
