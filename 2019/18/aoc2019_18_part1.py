_,E,F,M=set,enumerate,filter,{}
U=lambda x:_(F(str.islower,x))
for y,r in E(open("input.txt")):
 for x,c in E(r):M[x+y*1j]=c
L={c:x for x,c in M.items()}
W={x for x,c in M.items()if'#'==c}
K,D,C=U(L),{},{}
for k in{'@'}|K:
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
 z=tuple(sorted(v)+[p])
 if z in C:return C[z]+d
 s=min([1e9]+[S(v|g,t,a)for t,a,g,n in(D[p][t]for t in K-v)if not n-v]);C[z]=s;return s+d
print S(_(),'@',0)
