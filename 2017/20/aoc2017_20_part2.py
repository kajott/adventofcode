import re,collections as C
p=[map(int,re.findall('-?\d+',l))for l in open("input.txt")]
v,t=set(range(len(p))),333
while t:
 c=C.defaultdict(set);t-=1
 for i in v:
  z=p[i];c[tuple(z[:3])]|={i}
  for j in(3,4,5,0,1,2):z[j]+=z[j+3]
 for s in c.values():v-=s if len(s)>1else{-1}
print len(v)
