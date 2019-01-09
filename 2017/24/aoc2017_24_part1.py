from collections import*
B=[map(int,l.strip().split('/'))for l in open("input.txt")]
m=lambda s,p,v:max([s]+[m(s+sum(b),b[1-b.index(p)],v|{i})for i,b in enumerate(B)if p in b and not i in v])
print m(0,0,{-1})
