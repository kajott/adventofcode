from collections import*
S=defaultdict(set)
I=list(open("input.txt"))
for k,v in(map(str.strip,l.split('=>'))for l in I if'='in l):S[k]|={v}
x=sorted(I,key=len)[-1].strip();s=set()
for a in xrange(len(x)):
 for l in(1,2):s|={x[:a]+r+x[a+l:]for r in S[x[a:a+l]]}
print len(s)
