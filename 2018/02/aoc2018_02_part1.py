n={2:0,3:0}
for x in open("input.txt"):
 h={}
 for l in x:h[l]=h.get(l,0)+1
 for i in(2,3):n[i]+=i in h.values()
print n[2]*n[3]
