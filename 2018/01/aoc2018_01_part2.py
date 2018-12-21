from itertools import*
s,f=set(),0
for d in cycle([int(x.strip())for x in open("input.txt")]):
 f+=d
 if f in s:break
 s|={f}
print f
