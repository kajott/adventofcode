# 2023, Day 3: Gear Ratios


## Solution Notes

The tricky part here is coming up with an easy to handle data structure in which to store the input data for easy processing. In the end, what needs to be done is kind of a connected component analysis in horizontal direction, starting at the neighbor positions of the symbols, to retrieve the surrounding numbers.

My initial approach was to use the proven method of a coordinate-as-complex-number to character dictionary, and having a lookup function that "samples" a number at a specified position, if there is one. This does the job well; it even reduces the actual evaluations for both parts to one (lengthly) line each, albeit with lots of nested generator expressions containing nested loops. Still, the "sampling" function stood out as being quite long ... there has to be a better way?

There is another approach, after all: Parse numbers as such right at the beginning, and store them as _(row, start column, end column, value)_ tuples. This indeed simplifies the sampling function a lot (it's a one-liner now), but it makes the input parser more complex (it's no longer a one-liner) and complex numbers are out of the question, because we need to compare coordinates against intervals. In the end, this approach turned out to be significantly worse in terms of code size and, surprisingly, execution time too.

* Part 1, Python (complex number dictionary): 294 bytes, <100 ms
* Part 2, Python (complex number dictionary): 332 bytes, <100 ms
* Part 1, Python (list of spans): 355 bytes, ~800 ms
* Part 2, Python (list of spans): 399 bytes, ~400 ms
