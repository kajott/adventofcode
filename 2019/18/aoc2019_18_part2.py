_,E,F,M=set,enumerate,filter,{}
U=lambda x:_(F(str.islower,x))
for y,r in E(open("input.txt")):
 for x,c in E(r):M[x+y*1j]=c
L=lambda:{c:x for x,c in M.items()}
c=L()['@']
for y,o in zip((-1j,0,1j),("0#1","###","2#3")):
 for x,o in zip((-1,0,1),o):M[c+x+y]=o
L=L();W={x for x,c in M.items()if'#'==c}
B,K,D,C=list("0123"),U(L),{},{}
for k in _(B)|K:
 n={L[k]};f={};d=0;v=_(W);D[k]={}
 while n:
  c=n;n=_();v|=c
  for p in c:
   r={p-1j,p+1j,p-1,p+1}-v;n|=r
   for x in r:f[x]=p
 for j in K:
  v=_();d=0;p=L[j]
  while p in f:v|={M[p]};p=f[p];d+=1
  D[k][j]=(j,d,U(v),_(map(str.lower,F(str.isupper,v))))
def S(v,p,d):
 if v==K:return d
 z=tuple(sorted(v)+p)
 if z in C:return C[z]+d
 s=min(min([1e9]+[S(v|g,[t if q==u else q for q in p],a)for t,a,g,n in(D[u][t]for t in K-v)if not(n-v)and a])for i,u in E(p));C[z]=s;return s+d
print S(_(),B,0)
