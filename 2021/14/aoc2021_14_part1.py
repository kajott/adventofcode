f=open("input.txt")
P,R=f.readline().strip(),{};A=set(P)
for l in f:
 if' '<l:R[l[:2]]=l[6];A|={l[6]}
for t in range(10):
 for i in range(len(P)-1,0,-1):P=P[:i]+R.get(P[i-1:i+1],"")+P[i:]
F=[P.count(e)for e in A]
print max(F)-min(F)
