E,N=enumerate,[[*map(int,l.split(','))]for l in open("input.txt")]
B,O=0,lambda a,b:(min(a,b),max(a,b))
for i,(X,Y)in E(N):
 for u,v in N[i:]:
  x,u=O(X,u);y,v=O(Y,v);a=(u-x+1)*(v-y+1);k=a>B
  for j,(p,q)in E(N):
   s,t=N[j-1];p,s=O(p,s);q,t=O(q,t);k*=not(q-t)*(x<p<u)*(q<v)*(t>y)+(p-s)*(y<q<v)*(p<u)*(s>x)
   if k<1:break
  if k:B=a
print(B)
