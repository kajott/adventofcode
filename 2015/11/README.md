# 2015, Day 11: Corporate Policy


## Solution Notes

Implementing the rules is a little tedious, but workable; regular expressions help a lot for rules 2 and 3. Runtime performance is a bit lacking; maybe it can be proven that the valid passwords are always in the form `...xxyzz`, `...aabcc` etc., then it would be trivial to only enumerate passwords that follow this pattern.

* Part 1, Python: 276 bytes, ~150 ms
* Part 2, Python: 314 bytes, ~6 s
