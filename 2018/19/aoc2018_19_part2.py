_=range
import re
O,I,P,R={"addr":lambda r,a,b:r[a]+r[b],"addi":lambda r,a,b:r[a]+b,"mulr":lambda r,a,b:r[a]*r[b],"muli":lambda r,a,b:r[a]*b,"banr":lambda r,a,b:r[a]&r[b],"bani":lambda r,a,b:r[a]&b,"borr":lambda r,a,b:r[a]|r[b],"bori":lambda r,a,b:r[a]|b,"setr":lambda r,a,b:r[a],"seti":lambda r,a,b:a,"gtir":lambda r,a,b:a>r[b],"gtri":lambda r,a,b:r[a]>b,"gtrr":lambda r,a,b:r[a]>r[b],"eqir":lambda r,a,b:a==r[b],"eqri":lambda r,a,b:r[a]==b,"eqrr":lambda r,a,b:r[a]==r[b]},0,[],[1]+[0]*5
for l in open("input.txt"):
 n=map(int,re.findall('\d+',l));l=l.split()[0]
 if'#ip'==l:I=n[0]
 else:P+=[[O[l]]+n]
for x in _(99):o,a,b,d=P[R[I]];R[d]=o(R,a,b);R[I]+=1
N=max(R);print sum(x for x in _(1,N+1)if N%x<1)
