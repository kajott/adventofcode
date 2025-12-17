# [2019, Day 16: Flawed Frequency Transmission](https://adventofcode.com/2019/day/16)


## Solution Notes

Part 1 is a reasonably straightforward 650x650-element matrix-by-vector multiplication (at least for my input; other inputs may have different dimensions). The only part that needs some wrapping one's head around is setting up the transformation matrix, but that's perfectly manageable.

Part 2, however, is where the fun ends. Simply computing the result as usual is out of the question, as the matrix grows to 6.5M x 6.5M elements, making even highly-optimized C implementations unfeasible. Obviously, there has to be some kind of shortcut, but it's frustratingly hard to find. Interestingly enough, *when* the shortcut has been found, the solution for part 2 is actually simpler than part 1's.

<details><summary>There are two thing to note. (Spoilers!)</summary>

First, the transform matrix is an upper diagonal matrix, and its bottom half is particularily simple. For example, in an 8-element "FFT" transform:

    1 0 complicated
    0 1 1 0 0 stuff
    0 0 1  in these
    0 0 0 1 1  rows
    0 0 0 0 1 1 1 1
    0 0 0 0 0 1 1 1
    0 0 0 0 0 0 1 1
    0 0 0 0 0 0 0 1

As a result, the second half of the input signal can be trivially computed by summing elements together, starting at the end. In particular, the final digit of the vector never changes.

Second, the first seven digits of the input are constructed such that they point somewhere towards the *end* of the 6.5M-element result vector (in my case, at ~6M).

<details><summary>The solution can be found by combining these facts. (More Spoilers!)</summary>

If only the result of some position in the last half of the input is desired, *all elements before that can be ignored and do not need to be computed*. This is also true when performing the transform multiple times, so for all intents and purposes, we can just throw away the initial ~90% of the vector before computing anything. And for the remaining ~530k elements, the computation of the transform is rather simple, as described above.

</details></details>

* Part 1, Python (computing and "caching" the transform matrix first): 214 bytes, ~5 s
* Part 1, Python (computing the transform matrix on-the-fly): 185 bytes, ~10 s
* Part 2, Python: 179 bytes, ~10 s
