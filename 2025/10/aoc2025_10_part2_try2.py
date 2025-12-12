import math as M
V,O,R,Z=abs,min,range,zip
S=lambda i,r,f:O(S(i-1,[y-n*c for y,c in Z(r,C[i])],[n]+f)for n in R(U[i]+1))if i>=0 else 999 if any(y%N+(y<0)for y in r)else sum([y//N for y in r]+f)
def Q(p,t):
 a,b=A[p][p],A[t][p];g=M.gcd(a,b)
 if b:A[t]=[(v*a-u*b)//g for u,v in Z(A[p],A[t])]
G,W=0,lambda:[j for j in R(i,Y)if V(A[j][i])]
for L in open("input.txt"):
 B=[[*map(int,p[1:-1].split(','))]for p in L.split()[1:]];Y=len(T:=B.pop());X=len(B);A=[[r in b for b in B]for r in R(Y)];A+=[[O(y for r,y in Z(A,T)if r[j])for j in R(X)]]
 for r,y in Z(A,T):r+=[y]
 for i in R(O(X,Y)):
  if not(z:=W()):
   z=[j for j in R(i+1,X)if any(V(A[k][j])for k in R(i,Y))]
   if not z:break
   p=z[0];A=[r[:i]+r[p:p+1]+r[i:p]+r[p+1:]for r in A];z=W()
  p=O(z,key=lambda j:V(A[j][i]));A[p],A[i]=A[i],A[p];[Q(i,j)for j in R(i+1,Y)]
 while 1-any(A[-2]):del A[-2];Y-=1
 [Q(i,j)for i in R(Y-1,0,-1)for j in R(i)]
 N=M.lcm(*[V(A[i][i])for i in R(Y)])
 for i in R(Y):A[i]=[x*N//A[i][i]for x in A[i]]
 U=A[-1][Y:];C=[*Z(*A[:-1])][Y:];G+=S(X-Y-1,C.pop(),[])
print(G)
