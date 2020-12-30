import re
T=0
for x in open("input.txt"):
 o,r,s=[],[],[];p=o.pop
 for t in re.findall('\d+|[+*()]',x):
  if')'>t:o+=[t]
  elif'*'>t:
   while'('<o[-1]:r+=[p()]
   if')'>o[-1]:p()
  elif'0'>t:
   while o and o[-1]>'('and(o[-1]>'*'and'+'>t):r+=[p()]
   o+=[t]
  else:r+=[int(t)]
 for t in r+o[::-1]:
  if'+'==t:n=s.pop();s[-1]+=n
  elif'*'==t:n=s.pop();s[-1]*=n
  else:s+=[t]
 T+=s[0]
print T
