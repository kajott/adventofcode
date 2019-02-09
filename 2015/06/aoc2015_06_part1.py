_=range
import re
g=[[0]*1000for y in _(1000)]
for l in open("input.txt"):
 a,b,c,d=map(int,re.findall('\d+',l));m={'n':3,'f':0,' ':1}[l[6]]
 for y in _(a,c+1):
  for x in _(b,d+1):g[y][x]=(m>>g[y][x])&1
print sum(map(sum,g))
