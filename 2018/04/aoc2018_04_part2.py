import re,collections as C
s=C.defaultdict(lambda:60*[0])
for t,e in sorted(((int(l[6:17].translate(None," -:")),l[19:]) for l in open("input.txt"))):
 m=re.search('\d+',e);t%=100
 if m:g=int(m.group(0));continue
 if e[0]=='f':a=t;continue
 for m in range(a,t):s[g][m]+=1
g=max((max(v),k) for k,v in s.items())[1]
print g*max(x[::-1] for x in enumerate(s[g]))[1]
