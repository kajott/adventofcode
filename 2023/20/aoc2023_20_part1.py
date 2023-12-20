S,F,N,M,R=str.strip,{},{},{},{}
for l in open("input.txt"):
 n,o=l.split('->');n=S(n);t=n[0];n=n['a'>t:3];o=[*map(S,o.split(','))];M[n]=o
 if'a'>t:(F if'&'>t else N)[n]=0
 for d in o:R[d]=R.get(d,[])+[n]
N,A,B={n:{s:0 for s in R[n]}for n in N},0,0
for t in range(1000):
 q,c=[(0,0,'bro')],[0,0]
 while q:
  s,p,d=q.pop(0);c[p]+=1;o=1
  if d in F:o=1-p;p=F[d]=F[d]^o
  if d in N:N[d][s]=p;p=1-all(N[d].values())
  q+=[(d,p,n)for n in M.get(d,[])]*o
 A+=c[0];B+=c[1]
print(A*B)
