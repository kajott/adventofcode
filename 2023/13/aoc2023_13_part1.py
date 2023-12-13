A,C=0,lambda m:sum(i*(m[i-n:i]==m[i:i+n][::-1])for i,n in((i,min(i,len(m)-i))for i in range(1,len(m))))
for f in open("input.txt").read().split('\n\n'):M=f.strip().split('\n');A+=C(M)*100+C([*zip(*M)])
print(A)
