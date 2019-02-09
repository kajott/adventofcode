# 2015, Day 8: Matchsticks

Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

## Part 1

It is common in many programming languages to provide a way to escape special characters in strings. For example, [C](https://en.wikipedia.org/wiki/Escape_sequences_in_C), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), [Perl](http://perldoc.perl.org/perlop.html#Quote-and-Quote-like-Operators), [Python](https://docs.python.org/2.0/ref/strings.html), and even [PHP](http://php.net/manual/en/language.types.string.php#language.types.string.syntax.double) handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters _in the code representation of the string literal_ and the number of characters _in the in-memory string itself_.

For example:

*   `""` is `2` characters of code (the two double quotes), but the string contains zero characters.
*   `"abc"` is `5` characters of code, but `3` characters in the string data.
*   `"aaa\"aaa"` is `10` characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of `7` characters in the string data.
*   `"\x27"` is `6` characters of code, but the string itself contains just one - an apostrophe (`'`), escaped using hexadecimal notation.

Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are `\\` (which represents a single backslash), `\"` (which represents a lone double-quote character), and `\x` plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is _the number of characters of code for string literals_ minus _the number of characters in memory for the values of the strings_ in total for the entire file?

For example, given the four strings above, the total number of characters of string code (`2 + 5 + 10 + 6 = 23`) minus the total number of characters in memory for string values (`0 + 3 + 7 + 1 = 11`) is `23 - 11 = 12`.

Your puzzle answer was `1350`.

## Part 2

Now, let's go the other way. In addition to finding the number of characters of code, you should now _encode each code representation as a new string_ and find the number of characters of the new encoded representation, including the surrounding double quotes.

For example:

*   `""` encodes to `"\"\""`, an increase from `2` characters to `6`.
*   `"abc"` encodes to `"\"abc\""`, an increase from `5` characters to `9`.
*   `"aaa\"aaa"` encodes to `"\"aaa\\\"aaa\""`, an increase from `10` characters to `16`.
*   `"\x27"` encodes to `"\"\\x27\""`, an increase from `6` characters to `11`.

Your task is to find _the total number of characters to represent the newly encoded strings_ minus _the number of characters of code in each original string literal_. For example, for the strings above, the total encoded length (`6 + 9 + 16 + 11 = 42`) minus the characters in the original code representation (`23`, just like in the first part of this puzzle) is `42 - 23 = 19`.

Your puzzle answer was `2085`.


## Solution Notes

The good news is that both parts are solvable with one-liners. The bad news, however, is that part 1 requires evil `eval` to do this in the most compact way. Oh well ...

* Part 1, Python: 65 bytes, <100 ms
* Part 2, Python: 66 bytes, <100 ms
