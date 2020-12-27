import re;F=re.findall
I=open("input.txt").read()
R=[map(int,m)for m in F('(\d+)-(\d+)',I)]
S=0
for T in F('\d+,[0-9,]+',I):
 for n in map(int,T.split(',')):
  if any(a<=n<=b for a,b in R)<1:S+=n
print S
