M=0
for L in open("input.txt"):M=M and[M[i]*('Z'>L[i])+sum(M[x]*('Z'<L[x])for x in(i-1,i+1))for i in range(len(M)-1)]+[0]or[c>'A'for c in L]
print(sum(M))
