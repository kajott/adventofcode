S,P=''.join(format(int(x,16),'04b')for x in open("input.txt").read().strip()),[0]
A,M={0:sum,2:min,3:max},{5:1,6:-1,7:0}
def G(n):P[0]+=n;return int(S[P[0]-n:P[0]],2)
def D():
 t,v,x,q=G(6)&7,0,-1,[]
 if t==4:
  while x&16:x=G(5);v=v<<4|x&15
 elif G(1):q=[D()for x in range(G(11))]
 else:
  e=G(15);e+=P[0]
  while P[0]<e:q+=[D()]
 if t==1:
  v=1
  for p in q:v*=p
 elif t<4:v=A[t](q)
 elif t>4:v=cmp(q[0],q[1])==M[t]
 return v
print D()
