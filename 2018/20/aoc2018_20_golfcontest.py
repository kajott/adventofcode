S=set;D,N,p,s,e,q=S(),{'N':-1j,'E':1,'W':-1,'S':1j},{0},{0},S(),[]
for c in open("a").read()[1:-2]:
 if c=='|':e|=p;p=S(s)
 elif c=='(':q+=[(s,e)];s,e=S(p),S()
 elif c==')':p|=e;s,e=q.pop()
 else:o=N[c];D|={x+o for x in p};p={x+o*2for x in p}
d,a,q=0,S(),[{0}]
while q[d]:
 d+=1;q+=[S()]
 for x in q[d-1]:a|={x};q[d]|={x+o*2for o in N.values()if x+o in D}
 q[d]-=a
print d-1
print sum(len(z)for z in q[1000:])
