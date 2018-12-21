import re,collections as C
from operator import*
m=C.defaultdict(int)
for d,o,i,s,c,r in(re.match('(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]=?) (-?\d+)',x).groups()for x in open("input.txt")):
 if{'<':lt,'>':gt,'==':eq,'!=':ne,'>=':ge,'<=':le}[c](m[s],int(r)):m[d]+=int(i)*(1-2*(o<'i'))
print max(m.values())
