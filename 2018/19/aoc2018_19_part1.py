import re
O,I,P,R={"addr":lambda r,a,b:r[a]+r[b],"addi":lambda r,a,b:r[a]+b,"mulr":lambda r,a,b:r[a]*r[b],"muli":lambda r,a,b:r[a]*b,"banr":lambda r,a,b:r[a]&r[b],"bani":lambda r,a,b:r[a]&b,"borr":lambda r,a,b:r[a]|r[b],"bori":lambda r,a,b:r[a]|b,"setr":lambda r,a,b:r[a],"seti":lambda r,a,b:a,"gtir":lambda r,a,b:a>r[b],"gtri":lambda r,a,b:r[a]>b,"gtrr":lambda r,a,b:r[a]>r[b],"eqir":lambda r,a,b:a==r[b],"eqri":lambda r,a,b:r[a]==b,"eqrr":lambda r,a,b:r[a]==r[b]},0,[],[0]*6
for l in open("input.txt"):
 n=map(int,re.findall('\d+',l));l=l.split()[0]
 if l=='#ip':I=n[0]
 else:P+=[[O[l]]+n]
while 0<=R[I]<len(P):o,a,b,d=P[R[I]];R[d]=o(R,a,b);R[I]+=1
print R[0]
