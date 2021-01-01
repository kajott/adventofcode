import re
f=open("input.txt")
R,U,I={},{},{}
for l in(l.strip().replace(':','').split('|')for l in f):
 if not l[0]:break
 if'"'==l[0][-1]:R[int(l[0].split()[0])]=l[0][-2]
 else:l=[map(int,x.split())for x in l];n=l[0].pop(0);U[n]=l;I[n]=set(l[0]+(l[1]if len(l)>1else[]))
while U:
 for n in U:
  if set(R)>=I[n]:
   R[n]='|'.join([''.join('('+R[x]+')'if'|'in R[x]else R[x]for x in l)for l in U[n]]);del U[n];break
print sum(bool(re.match(R[0]+'$',l))for l in f)
