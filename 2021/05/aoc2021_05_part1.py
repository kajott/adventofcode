import re
R,M=range,{}
N=map(int,re.findall('\d+',open("input.txt").read()))
for a,b,c,d in[N[i:i+4]for i in R(0,len(N),4)]:
 L=[(a,x)for x in R(min(b,d),max(b,d)+1)]if a==c else[(x,b)for x in R(min(a,c),max(a,c)+1)]if b==d else[]
 for p in L:M[p]=M.get(p,0)+1
print sum(c>1for c in M.values())
