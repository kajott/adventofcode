D,N=set(),{'N':-1j,'E':1,'W':-1,'S':1j};p=[0]
for c in open("input.txt").read().strip("^$\n"):
 if c=='|':p[-1]=p[-2]
 elif c=='(':p+=[p[-1]]
 elif c==')':p.pop()
 else:o=N[c];D.add(p[-1]+o);p[-1]+=2*o
d,a,q=0,set(),[{0}]
while q[d]:
 d+=1;q+=[set()]
 for x in q[d-1]:a.add(x);[q[d].add(x+2*o)for o in N.values()if x+o in D]
 q[d]-=a
print d-1
print sum(len(z)for z in q[1000:])
