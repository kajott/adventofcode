import re
F=open("input.txt")
D,C={},{}
for l in(l.strip().replace(':','').split('|')for l in F):
 if not l[0]:break
 if'"'==l[0][-1]:D[int(l[0].split()[0])]=l[0][-2]
 else:l=[map(int,x.split())for x in l];n=l[0].pop(0);C[n]=l
C[8]=[[42],[42,8]]
C[11]=[[42,31],[42,11,31]]
def M(r,i):
 if i<0 or i>=len(S):return[]
 if r in D:return[i+1]if S[i]==D[r]else[]
 m=[]
 for v in C[r]:
  b=[i]
  for s in v:
   a=b;b=[]
   for k in a:b+=M(s,k)
  m+=b
 return m
n=0
for S in F:n+=len(S.strip())in M(0,0)
print n
