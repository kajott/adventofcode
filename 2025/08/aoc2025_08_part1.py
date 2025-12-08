E,S,T=enumerate,sorted,tuple
N=[T(map(int,l.split(',')))for l in open("input.txt")]
D=[(sum((u-v)**2 for u,v in zip(a,b)),a,b)for i,a in E(N)for j,b in E(N[i+1:],i+1)]
C={a:{a}for a in N}
for _,a,b in S(D)[:1000]:
 n=C[a]|C[b]
 for k in n:C[k]=n
C={T(S(C[n]))for n in C}
a,b,c=S(map(len,C))[-3:];print(a*b*c)
