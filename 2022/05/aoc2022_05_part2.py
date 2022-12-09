import re
I,S=open("input.txt").read(),[];L=I.split("\n")
for c in range(99):c=[x for x in(r[c:c+1]for r in L)if'@'<x<'['];S+=[c]*bool(c)
for m in re.findall("m.*?(\d+).*?(\d+).*?(\d+)",I):n,f,t=map(int,m);f=S[f-1];x=f[:n];del f[:n];S[t-1][0:0]=x
print''.join(c[0]for c in S)
