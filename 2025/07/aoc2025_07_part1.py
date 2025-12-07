C=0
for L in open("input.txt"):
 if'S'in L:B={L.index('S')}
 C+=len(s:={x for x in B if'Z'<L[x]});B={x+d for x in s for d in(-1,1)}|B-s
print(C)
