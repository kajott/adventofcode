# 2021, Day 8: Seven Segment Search

You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit [seven-segment displays](https://en.wikipedia.org/wiki/Seven-segment_display) in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

## Part 1

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named `a` through `g`:

      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....
    
      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
    

So, to render a `1`, only segments `c` and `f` would be turned on; the rest would be off. To render a `7`, only segments `a`, `c`, and `f` would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires `a` through `g`, but those wires are connected to segments _randomly_. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits _within_ a display use the same connections, though.)

So, you might know that only signal wires `b` and `g` are turned on, but that doesn't mean _segments_ `b` and `g` are turned on: the only digit that uses two segments is `1`, so it must mean segments `c` and `f` are meant to be on. With just that information, you still can't tell which wire (`b`/`g`) goes to which segment (`c`/`f`). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of _all ten unique signal patterns_ you see, and then write down a single _four digit output value_ (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
    cdfeb fcadb cdfeb cdbaf

(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten _unique signal patterns_, a `|` delimiter, and finally the _four digit output value_. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because `7` is the only digit that uses three segments, `dab` in the above example means that to render a `7`, signal lines `d`, `a`, and `b` are on. Because `4` is the only digit that uses four segments, `eafb` means that to render a `4`, signal lines `e`, `a`, `f`, and `b` are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (`cdfeb fcadb cdfeb cdbaf`) use five segments and are more difficult to deduce.

For now, _focus on the easy digits_. Consider this larger example:

    be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
    fdgacbe cefdb cefbgd gcbe
    edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
    fcgedb cgb dgebacf gc
    fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
    cg cg fdcagb cbg
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
    efabcd cedba gadfec cb
    aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
    gecf egdcabf bgf bfgea
    fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
    gebdcfa ecba ca fadegcb
    dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
    cefg dcbef fcge gbcadfe
    bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
    ed bcgafe cdgba cbgef
    egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
    gbdfcae bgc cg cgb
    gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
    fgae cfgab fg bagce
    

Because the digits `1`, `4`, `7`, and `8` each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting _only digits in the output values_ (the part after `|` on each line), in the above example, there are `_26_` instances of digits that use a unique number of segments (highlighted above).

_In the output values, how many times do digits `1`, `4`, `7`, or `8` appear?_

Your puzzle answer was `294`.

## Part 2

Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
    cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

     dddd
    e    a
    e    a
     ffff
    g    b
    g    b
     cccc
    

So, the unique signal patterns would correspond to the following digits:

*   `acedgfb`: `8`
*   `cdfbe`: `5`
*   `gcdfa`: `2`
*   `fbcad`: `3`
*   `dab`: `7`
*   `cefabd`: `9`
*   `cdfgeb`: `6`
*   `eafb`: `4`
*   `cagedb`: `0`
*   `ab`: `1`

Then, the four digits of the output value can be decoded:

*   `cdfeb`: _`5`_
*   `fcadb`: _`3`_
*   `cdfeb`: _`5`_
*   `cdbaf`: _`3`_

Therefore, the output value for this entry is _`5353`_.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

*   `fdgacbe cefdb cefbgd gcbe`: `8394`
*   `fcgedb cgb dgebacf gc`: `9781`
*   `cg cg fdcagb cbg`: `1197`
*   `efabcd cedba gadfec cb`: `9361`
*   `gecf egdcabf bgf bfgea`: `4873`
*   `gebdcfa ecba ca fadegcb`: `8418`
*   `cefg dcbef fcge gbcadfe`: `4548`
*   `ed bcgafe cdgba cbgef`: `1625`
*   `gbdfcae bgc cg cgb`: `8717`
*   `fgae cfgab fg bagce`: `4315`

Adding all of the output values in this larger example produces _`61229`_.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. _What do you get if you add up all of the output values?_

Your puzzle answer was `973292`.


## Solution Notes

Part 1 is a trivial training task, nothing to see there.

Part 2 is a different beast altogether. Programming-wise, it isn't too bad (golf-specific issues notwithstanding); the complicated part is coming up with a recipe on how to deduce the numbers from the observed patterns. There are certainly several ways to approach this, and I'm not sure whether mine is the optimal one, but here it is (spoilers ahead!):

- Numbers #1, #7, #4 and #8 can be trivially deduced by the pattern length (2, 3, 4, and 8, respectively), as already explained in the task description.
- Of the three patterns with length 5, number #3 is the only one that is a true superset of #1.
- Of the other two patterns of length 5, number #5 contains segment B (which is present in #4, but not #3), while number #2 doesn't.
- The three length-6 patterns are all missing exactly one of the segments: #6 is missing C (which is present in #3, but not #5), #9 is missing E (which is present in #2, but not #3), and #0 is missing D (which doesn't need to be determined, because #0 is the only remaining number at that point).

Turning all of this into a compact implementation wasn't trivial. It all revolves around global variables for the current set of patterns and the current pattern-to-number map, and a function that takes the target number, pattern length and a condition function as parameters; it locates the one pattern that has the correct length and fulfills the condition, enters it into the map, and returns the pattern as a set. Using these return values and set arithmetics, the necessary deduction operations can be done easily. It's still an awful lot of `lambda`s, and one _very_ long line, but it's not the most complicated thing either.

* Part 1, Python: 118 bytes, <100 ms
* Part 2, Python: 455 bytes, <100 ms
