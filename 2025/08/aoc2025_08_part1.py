S,T=sorted,tuple
N=[T(map(int,l.split(',')))for l in open("input.txt")]
D=S((sum((u-v)**2 for u,v in zip(a,b)),a,b)for i,a in enumerate(N)for b in N[i+1:])
C={a:{a}for a in N}
for _,a,b in D[:1000]:
 n=C[a]|C[b]
 for k in n:C[k]=n
a,b,c=S(map(len,{T(S(C[n]))for n in C}))[-3:];print(a*b*c)
