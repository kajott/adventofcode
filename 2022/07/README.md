# [2022, Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7)

The input consists of a (typically) 1000-line trace of a terminal session on a UNIX-like system. The only commands that occur are `cd ..`, `cd` with some single directory name, and `ls`. The output of `ls` only lists file names and sizes; subdirectories are listed as `dir` instead of a size. File and directory names are random character sequences following the 8.3 scheme.

**Part 1** asks for all directories with a total size of less than some fixed threshold.

**Part 2** asks for the smallest directory with a total size _above_ some threshold.


## Solution Notes

This task is not a complicated one at all, but the devil's in the details and there are various ways to introduce subtle bugs.

What definitely helps is that the input is constructed in a non-malicious way; specifically, there's exactly one `cd /` at the beginning of the file (which means that it can be ignored completely, and `ls` is called exactly *once* for each directory. This means that a separate data structure that keeps track of "visited" directories is not necessary; we can just add all file sizes we encounter to their parent directories right during parsing.

I combined the solutions for both parts into a single file, because only the final `print` statement would be different between the individual parts' solutions.

* Parts 1+2, Python: 261 bytes, <100 ms
