import re
from operator import*
m={}
for d,o,i,s,c,r in(re.match('(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]=?) (-?\d+)',x).groups()for x in open("input.txt")):
 if{'<':lt,'>':gt,'==':eq,'!=':ne,'>=':ge,'<=':le}[c](m.get(s,0),int(r)):m[d]=m.get(d,0)+int(i)*(1-2*(o<'i'))
print max(m.values())
