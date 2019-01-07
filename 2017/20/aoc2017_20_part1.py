import re
a=[map(int,re.findall('-?\d+',l))for l in open("input.txt")]
for t in range(333):
 for p in a:
  for i in(3,4,5,0,1,2):p[i]+=p[i+3]
print min((sum(abs(x)for x in p[:3]),i)for i,p in enumerate(a))[-1]
