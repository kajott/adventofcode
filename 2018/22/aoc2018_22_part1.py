_=range
import re
n,w,h=map(int,re.findall('\d+',open("input.txt").read()))
m=20183;g=[[(x*16807+n)%m for x in _(w+1)]]+[[((y+1)*48271+n)%m]+w*[0]for y in _(h)]
for y in _(h):
 for x in _(w):g[y+1][x+1]=(g[y][x+1]*g[y+1][x]+n)%m
g[h][w]=0
print sum(sum(c%3for c in r)for r in g)
