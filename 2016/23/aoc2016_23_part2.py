import re
n=sorted(map(int,re.findall('\d+',open("input.txt").read())))
print 479001600+n[-1]*n[-2]
