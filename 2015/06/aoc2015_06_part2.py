_=range
import re
g=[[0]*1000for y in _(1000)]
for l in open("input.txt"):
 a,b,c,d=map(int,re.findall('\d+',l));m={'n':1,'f':-1,' ':2}[l[6]]
 for y in _(a,c+1):
  for x in _(b,d+1):g[y][x]=max(0,m+g[y][x])
print sum(map(sum,g))
