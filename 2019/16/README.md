# 2019, Day 16: Flawed Frequency Transmission

You're 3/4ths of the way through the [gas giants](https://en.wikipedia.org/wiki/Gas_giant). Not only do roundtrip signals to Earth take five hours, but the signal quality is quite bad as well. You can clean up the signal with the Flawed Frequency Transmission algorithm, or _FFT_.

## Part 1

As input, FFT takes a list of numbers. In the signal you received (your puzzle input), each number is a single digit: data like `15243` represents the sequence `1`, `5`, `2`, `4`, `3`.

FFT operates in repeated _phases_. In each phase, a new list is constructed with the same length as the input list. This new list is also used as the input for the next phase.

Each element in the new list is built by multiplying every value in the input list by a value in a repeating _pattern_ and then adding up the results. So, if the input list were `9, 8, 7, 6, 5` and the pattern for a given element were `1, 2, 3`, the result would be `9*1 + 8*2 + 7*3 + 6*1 + 5*2` (with each input element on the left and each value in the repeating pattern on the right of each multiplication). Then, only the ones digit is kept: `38` becomes `8`, `-17` becomes `7`, and so on.

While each element in the output array uses all of the same input array elements, the actual repeating pattern to use depends on _which output element_ is being calculated. The base pattern is `0, 1, 0, -1`. Then, repeat each value in the pattern a number of times equal to the _position in the output list_ being considered. Repeat once for the first element, twice for the second element, three times for the third element, and so on. So, if the third element of the output list is being calculated, repeating the values would produce: `0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1`.

When applying the pattern, skip the very first value exactly once. (In other words, offset the whole pattern left by one.) So, for the second element of the output list, the actual pattern used would be: `0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1, ...`.

After using this process to calculate each element of the output list, the phase is complete, and the output list of this phase is used as the new input list for the next phase, if any.

Given the input signal `12345678`, below are four phases of FFT. Within each phase, each output digit is calculated on a single line with the result at the far right; each multiplication operation shows the input digit on the left and the pattern value on the right:

    Input signal: 12345678
    
    1*1  + 2*0  + 3*-1 + 4*0  + 5*1  + 6*0  + 7*-1 + 8*0  = 4
    1*0  + 2*1  + 3*1  + 4*0  + 5*0  + 6*-1 + 7*-1 + 8*0  = 8
    1*0  + 2*0  + 3*1  + 4*1  + 5*1  + 6*0  + 7*0  + 8*0  = 2
    1*0  + 2*0  + 3*0  + 4*1  + 5*1  + 6*1  + 7*1  + 8*0  = 2
    1*0  + 2*0  + 3*0  + 4*0  + 5*1  + 6*1  + 7*1  + 8*1  = 6
    1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*1  + 7*1  + 8*1  = 1
    1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*1  + 8*1  = 5
    1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*0  + 8*1  = 8
    
    After 1 phase: 48226158
    
    4*1  + 8*0  + 2*-1 + 2*0  + 6*1  + 1*0  + 5*-1 + 8*0  = 3
    4*0  + 8*1  + 2*1  + 2*0  + 6*0  + 1*-1 + 5*-1 + 8*0  = 4
    4*0  + 8*0  + 2*1  + 2*1  + 6*1  + 1*0  + 5*0  + 8*0  = 0
    4*0  + 8*0  + 2*0  + 2*1  + 6*1  + 1*1  + 5*1  + 8*0  = 4
    4*0  + 8*0  + 2*0  + 2*0  + 6*1  + 1*1  + 5*1  + 8*1  = 0
    4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*1  + 5*1  + 8*1  = 4
    4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*1  + 8*1  = 3
    4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*0  + 8*1  = 8
    
    After 2 phases: 34040438
    
    3*1  + 4*0  + 0*-1 + 4*0  + 0*1  + 4*0  + 3*-1 + 8*0  = 0
    3*0  + 4*1  + 0*1  + 4*0  + 0*0  + 4*-1 + 3*-1 + 8*0  = 3
    3*0  + 4*0  + 0*1  + 4*1  + 0*1  + 4*0  + 3*0  + 8*0  = 4
    3*0  + 4*0  + 0*0  + 4*1  + 0*1  + 4*1  + 3*1  + 8*0  = 1
    3*0  + 4*0  + 0*0  + 4*0  + 0*1  + 4*1  + 3*1  + 8*1  = 5
    3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*1  + 3*1  + 8*1  = 5
    3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*1  + 8*1  = 1
    3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*0  + 8*1  = 8
    
    After 3 phases: 03415518
    
    0*1  + 3*0  + 4*-1 + 1*0  + 5*1  + 5*0  + 1*-1 + 8*0  = 0
    0*0  + 3*1  + 4*1  + 1*0  + 5*0  + 5*-1 + 1*-1 + 8*0  = 1
    0*0  + 3*0  + 4*1  + 1*1  + 5*1  + 5*0  + 1*0  + 8*0  = 0
    0*0  + 3*0  + 4*0  + 1*1  + 5*1  + 5*1  + 1*1  + 8*0  = 2
    0*0  + 3*0  + 4*0  + 1*0  + 5*1  + 5*1  + 1*1  + 8*1  = 9
    0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*1  + 1*1  + 8*1  = 4
    0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*1  + 8*1  = 9
    0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*0  + 8*1  = 8
    
    After 4 phases: 01029498
    

Here are the first eight digits of the final output list after 100 phases for some larger inputs:

*   `80871224585914546619083218645595` becomes `24176176`.
*   `19617804207202209144916044189917` becomes `73745418`.
*   `69317163492948606335995924319873` becomes `52432133`.

After _100_ phases of FFT, _what are the first eight digits in the final output list?_

Your puzzle answer was `15841929`.

## Part 2

Now that your FFT is working, you can decode the _real signal_.

The real signal is your puzzle input _repeated 10000 times_. Treat this new signal as a single input list. Patterns are still calculated as before, and 100 phases of FFT are still applied.

The _first seven digits_ of your initial input signal also represent the _message offset_. The message offset is the location of the eight-digit message in the final output list. Specifically, the message offset indicates _the number of digits to skip_ before reading the eight-digit message. For example, if the first seven digits of your initial input signal were `1234567`, the eight-digit message would be the eight digits after skipping 1,234,567 digits of the final output list. Or, if the message offset were `7` and your final output list were `98765432109876543210`, the eight-digit message would be `21098765`. (Of course, your real message offset will be a seven-digit number, not a one-digit number like `7`.)

Here is the eight-digit message in the final output list after 100 phases. The message offset given in each input has been highlighted. (Note that the inputs given below are repeated 10000 times to find the actual starting input lists.)

*   __`0303673`__`2577212944063491565474664` becomes `84462026`.
*   __`0293510`__`9699940807407585447034323` becomes `78725270`.
*   __`0308177`__`0884921959731165446850517` becomes `53553731`.

After repeating your input signal 10000 times and running 100 phases of FFT, _what is the eight-digit message embedded in the final output list?_

Your puzzle answer was `39011547`.


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
