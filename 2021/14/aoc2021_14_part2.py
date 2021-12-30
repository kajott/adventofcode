import collections as C;D=C.defaultdict
f=open("input.txt")
P,R,H,F="-"+f.readline().strip()+"-",{},D(int),D(int)
for l in f:
 if' '<l:R[l[:2]]=l[6]
for a,b in zip(P,P[1:]):H[a+b]+=1
for t in range(40):
 O=H.items();H=D(int)
 for c,f in O:
  if c in R:H[c[0]+R[c]]+=f;H[R[c]+c[1]]+=f
  else:H[c]+=f
for c,f in H.items():F[c[0]]+=f
del F["-"];F=F.values()
print max(F)-min(F)
