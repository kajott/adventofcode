# 2015, Day 15: Science for Hungry People


## Solution Notes

I opted for a recursive solution to enumerate all possible combinations.

Summing up the total properties is effectively a matrix-vector product; however, clamping the results to zero is really necessary, because otherwise the product ("total score") might get bogus values if exactly two or four properties are negative.

The difference between part 1 and part 2 is very small: For part 2, simply force a recipe's score to zero if the calorie sum is not exactly 500.

* Part 1, Python: 253 bytes, ~1 s
* Part 2, Python: 263 bytes, ~1 s
