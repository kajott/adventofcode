# 2024, Day 19: Linen Layout

Today, The Historians take you up to the [hot springs](../../2023/12) on Gear Island! Very [suspiciously](https://www.youtube.com/watch?v=ekL881PJMjI), absolutely nothing goes wrong as they begin their careful search of the vast field of helixes.

Could this _finally_ be your chance to visit the [onsen](https://en.wikipedia.org/wiki/Onsen) next door? Only one way to find out.

After a brief conversation with the reception staff at the onsen front desk, you discover that you don't have the right kind of money to pay the admission fee. However, before you can leave, the staff get your attention. Apparently, they've heard about how you helped at the hot springs, and they're willing to make a deal: if you can simply help them _arrange their towels_, they'll let you in for _free_!

## Part 1

Every towel at this onsen is marked with a _pattern of colored stripes_. There are only a few patterns, but for any particular pattern, the staff can get you as many towels with that pattern as you need. Each stripe can be _white_ (`w`), _blue_ (`u`), _black_ (`b`), _red_ (`r`), or _green_ (`g`). So, a towel with the pattern `ggr` would have a green stripe, a green stripe, and then a red stripe, in that order. (You can't reverse a pattern by flipping a towel upside-down, as that would cause the onsen logo to face the wrong way.)

The Official Onsen Branding Expert has produced a list of _designs_ - each a long sequence of stripe colors - that they would like to be able to display. You can use any towels you want, but all of the towels' stripes must exactly match the desired design. So, to display the design `rgrgr`, you could use two `rg` towels and then an `r` towel, an `rgr` towel and then a `gr` towel, or even a single massive `rgrgr` towel (assuming such towel patterns were actually available).

To start, collect together all of the available towel patterns and the list of desired designs (your puzzle input). For example:

    r, wr, b, g, bwu, rb, gb, br
    
    brwrr
    bggr
    gbbr
    rrbgbr
    ubwu
    bwurrg
    brgr
    bbrgwb

The first line indicates the available towel patterns; in this example, the onsen has unlimited towels with a single red stripe (`r`), unlimited towels with a white stripe and then a red stripe (`wr`), and so on.

After the blank line, the remaining lines each describe a design the onsen would like to be able to display. In this example, the first design (`brwrr`) indicates that the onsen would like to be able to display a black stripe, a red stripe, a white stripe, and then two red stripes, in that order.

Not all designs will be possible with the available towels. In the above example, the designs are possible or impossible as follows:

*   `brwrr` can be made with a `br` towel, then a `wr` towel, and then finally an `r` towel.
*   `bggr` can be made with a `b` towel, two `g` towels, and then an `r` towel.
*   `gbbr` can be made with a `gb` towel and then a `br` towel.
*   `rrbgbr` can be made with `r`, `rb`, `g`, and `br`.
*   `ubwu` is _impossible_.
*   `bwurrg` can be made with `bwu`, `r`, `r`, and `g`.
*   `brgr` can be made with `br`, `g`, and `r`.
*   `bbrgwb` is _impossible_.

In this example, _`6`_ of the eight designs are possible with the available towel patterns.

To get into the onsen as soon as possible, consult your list of towel patterns and desired designs carefully. _How many designs are possible?_

Your puzzle answer was `265`.

## Part 2

The staff don't really like some of the towel arrangements you came up with. To avoid an endless cycle of towel rearrangement, maybe you should just give them every possible option.

Here are all of the different ways the above example's designs can be made:

`brwrr` can be made in two different ways: `b`, `r`, `wr`, `r` _or_ `br`, `wr`, `r`.

`bggr` can only be made with `b`, `g`, `g`, and `r`.

`gbbr` can be made 4 different ways:

*   `g`, `b`, `b`, `r`
*   `g`, `b`, `br`
*   `gb`, `b`, `r`
*   `gb`, `br`

`rrbgbr` can be made 6 different ways:

*   `r`, `r`, `b`, `g`, `b`, `r`
*   `r`, `r`, `b`, `g`, `br`
*   `r`, `r`, `b`, `gb`, `r`
*   `r`, `rb`, `g`, `b`, `r`
*   `r`, `rb`, `g`, `br`
*   `r`, `rb`, `gb`, `r`

`bwurrg` can only be made with `bwu`, `r`, `r`, and `g`.

`brgr` can be made in two different ways: `b`, `r`, `g`, `r` _or_ `br`, `g`, `r`.

`ubwu` and `bbrgwb` are still impossible.

Adding up all of the ways the towels in this example could be arranged into the desired designs yields _`16`_ (`2 + 1 + 4 + 6 + 1 + 2`).

They'll let you into the onsen as soon as you have the list. _What do you get if you add up the number of different ways you could make each design?_

Your puzzle answer was `752461716635602`.

## Solution Notes

Part 1's task can be done directly with regular expressions, so unsurprisingly, the best solution for that is to turn the input pattern list into a regex of form `/(r|wr|b|g|...|br)+$/` and check if that matches.

For part 2, the task of the regular expression matcher needs to be spelled out "by hand" in the form of a rather basic DFS with memoization.

Fun fact: Part 2's solution can be turned into part 1 simply by replacing the `abs()` call with `any()`.

* Part 1, Python: 125 bytes, <100 ms
* Part 2, Python: 206 bytes, ~500 ms
