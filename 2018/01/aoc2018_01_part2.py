from itertools import*
s,f=set(),0
for d in cycle(map(int,open("input.txt"))):
 f+=d
 if f in s:break
 s|={f}
print f
