import itertools as I
s,f=set(),0
for d in I.cycle([int(x.strip()) for x in open("input.txt")]):
 f+=d
 if f in s:break
 s.add(f)
print f
