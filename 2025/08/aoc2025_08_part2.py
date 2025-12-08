N=[tuple(map(int,l.split(',')))for l in open("input.txt")]
D=sorted((sum((u-v)**2 for u,v in zip(a,b)),a,b)for i,a in enumerate(N)for b in N[i+1:])
S,C={*N},{a:{a}for a in N}
for _,a,b in D:
 n=C[a]|C[b]
 for k in n:C[k]=n
 if S==n:break
print(a[0]*b[0])
