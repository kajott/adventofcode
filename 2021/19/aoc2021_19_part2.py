import re
L,T,S,C=len,tuple,[],[(0,0,0)]
for n in(map(int,re.findall('-?\d+',l))for l in open("input.txt")):
 l=L(n)
 if l==1:S+=[set()]
 if l==3:S[-1]|={T(n)}
def J(a,b):
 for r in range(48):
  o=[r>>4];o+=[r&1];o[1]+=o[1]>=o[0];o+=[3-sum(o)];m=[1-(r&2),1-(r&4)/2,1-(r&8)/4];h={}
  for i in a:
   for j in b:
    d=T(i[k]-j[o[k]]*m[k]for k in(0,1,2));f=h.get(d,0)+1;h[d]=f
    if f>11:
     for p in b:a|={T(p[o[k]]*m[k]+d[k]for k in(0,1,2))}
     return d
while L(S)>1:
 for i in range(1,L(S)):
  d=J(S[0],S[i])
  if d:C+=[d];del S[i];break
print max(sum(abs(a[k]-b[k])for k in(0,1,2))for a in C for b in C)
