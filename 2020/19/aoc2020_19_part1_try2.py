import re
F=open("input.txt")
D,C={},{}
for l in(l.strip().replace(':','').split('|')for l in F):
 if not l[0]:break
 if'"'==l[0][-1]:D[int(l[0].split()[0])]=l[0][-2]
 else:l=[map(int,x.split())for x in l];n=l[0].pop(0);C[n]=l
def M(r,i):
 if i<0 or i>=len(S):return-1
 if r in D:return i+1if S[i]==D[r]else-1
 for v in C[r]:
  j=i
  for r in v:j=M(r,j)
  if j>0:return j
 return-1
n=0
for S in F:n+=M(0,0)==len(S.strip())
print n
