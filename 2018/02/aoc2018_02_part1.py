import collections as C
n={2:0,3:0}
for x in open("input.txt"):
 h=C.defaultdict(int)
 for l in x:h[l]+=1
 for i in (2,3):n[i]+=int(i in h.values())
print n[2]*n[3]
