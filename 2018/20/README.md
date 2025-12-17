# 2018, Day 20: A Regular Map


## Solution Notes

This is a rather frustrating puzzle, simply because there are two ways to solve it: A simple way that ignores most of the complications of regular expression expansion, yet works for AoC's input sequences for reasons I don't quite understand; and a "proper" way that is much more complex to grasp.

I initially went for the second way, but had an extremely inefficient recursive implementation that only worked for the example inputs. Seeing that others solved this puzzle using simple iteration and a stack, I was seduced onto the simple way. This got me the points for the contest, but I wasn't satisfied that even simple tests like `^EEE(N|SSS)EEEE$` got the wrong answers, so I elaborated some more (and, frankly, took a note or two from other implementations) and finally got to a proper solution.

I participated in the "advent of golf" contest too; the version I submitted there is even slightly shorter than my normal version, but it doesn't use my usual `input.txt` file and expects the input to end in exactly one Unix newline, so I'm not using this for my standard repository here.

Both parts are combined here, because part 2 is just an additional line at the end.

* Parts 1+2, Python (shortcut): 368 bytes, ~350 ms
* Parts 1+2, Python (correct): 423 bytes, ~350 ms
