#!/usr/bin/env python2
import re

for line in open("input2.txt"):
    nums = map(int, re.findall('\d+', line))
    print(nums)

allnums = map(int, re.findall('\d+', open("input2.txt").read()))
