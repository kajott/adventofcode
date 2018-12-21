_=range
import re
from collections import*
d=defaultdict(int)
for i,x,y,w,h in(map(int,re.findall('\d+',x))for x in open("input.txt")):
 for y in _(y,y+h):
  for j in _(x,x+w):d[(j,y)]+=1
print sum(v>1for v in d.values())
