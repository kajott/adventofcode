# 2023, Day 1: Trebuchet?!

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all _fifty stars_ by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants _one star_. Good luck!

You try to ask why they can't just use a [weather machine](../../2015/01) ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a [trebuchet](https://en.wikipedia.org/wiki/Trebuchet) ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been _amended_ by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

## Part 1

The newly-improved calibration document consists of lines of text; each line originally contained a specific _calibration value_ that the Elves now need to recover. On each line, the calibration value can be found by combining the _first digit_ and the _last digit_ (in that order) to form a single _two-digit number_.

For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    

In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces _`142`_.

Consider your entire calibration document. _What is the sum of all of the calibration values?_

Your puzzle answer was `54450`.

## Part 2

Your calculation isn't quite right. It looks like some of the digits are actually _spelled out with letters_: `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine` _also_ count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    

In this example, the calibration values are `29`, `83`, `13`, `24`, `42`, `14`, and `76`. Adding these together produces _`281`_.

_What is the sum of all of the calibration values?_

Your puzzle answer was `54265`.

## Solution Notes

Part 2 of this task is surprisingly complex for a day-one puzzle. There are quite a few special cases that need to be covered, specifically around the question how to deal with overlapping numbers (e.g. `eightwo`). What the description inconveniently fails to mention, and the test data for part 2 fails to check in a meaningful way either, is that those are supposed to count as _both_, i.e. `eightwo` = `82`. In the end, the only proper solution is to either compile a list of **all** occurrences of any digits or numerals and pick the first and last of them; or (and this is what I ultimately used) search specifically for the _first and last_ occurrences of any digit or numeral and combine those.

* Part 1, Python: 88 bytes, <100 ms
* Part 2, Python: 246 bytes, <100 ms
