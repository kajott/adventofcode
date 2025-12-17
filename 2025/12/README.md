# [2025, Day 12: Christmas Tree Farm](https://adventofcode.com/2025/day/12)


## Solution Notes

This task is just pure evil. You may be tempted to actually come up with an (already extraordinarily complicated) solution for the example, only to find that the actual input calls for grid sizes around 50x50, with several dozens of tiles per shape, and there's over 1000 of them. No way to solve this easily, and I doubt that there's a nice library to do that either. However, as it turns out that it's all just a ruse ...

<details>
<summary>Spoiler <em>(click to expand)</em></summary>
... and simply comparing the areas of the puzzle pieces and the target area is sufficient.
</details>
&nbsp;

* Part 1, Python: 198 bytes, <100 ms
