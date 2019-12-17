M=dict(enumerate(map(int,open("input.txt").read().split(','))))
D,R,G,L,P=[0,-1j,1j,-1,1],[0,2,1,4,3],{0:2},0,[0]
def W(d):
 global L,P;L+=D[d];p=r=0
 while r<1:
  o=M[p];l=map(int,str(o)[-3::-1]+"000");o%=100;n=int("0331122331"[o]);i,j,k=[M.get(p+x,0)for x,m in zip((1,2,3),l)];a,b=[(M.get(x,0)if m-1else x)for x,m in zip((i,j),l)];p+=n+1
  if o<2:M[k]=a+b
  elif o<3:M[k]=a*b
  elif o<4:M[i]=d
  elif o<5:G[L]=r=a+1
  elif o>7:M[k]=a==b
  elif o>6:M[k]=a<b
  elif(o>5)^(a!=0):p=b
 if r>2:print len(P)
 if r<2:L-=D[d]
 elif d==R[P[-1]]:P.pop()
 else:P+=[d]
 return r
def E():
 f=R[P[-1]];[E()for d in(1,3,2,4)if d!=f and G.get(L+D[d])!=1and W(d)>1]
 if f:W(f)
E()
