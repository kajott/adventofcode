import re
from collections import *
d=defaultdict(int)
for i,x,y,w,h in (map(int,re.findall('\d+',x)) for x in open("input.txt")):
 for y in xrange(y,y+h):
  for j in xrange(x,x+w): d[(j,y)]+=1
print sum(1 for v in d.values() if v>1)
