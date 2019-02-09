import re
print sum(map(int,re.findall('-?\d+',open("input.txt").read())))
