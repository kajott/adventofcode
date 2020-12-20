n=0
for G in open("input.txt").read().split("\n\n"):
 Z=map(set,G.strip().split("\n"));d=Z.pop()
 for p in Z:d&=p
 n+=len(d)
print n
