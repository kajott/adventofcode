import re,collections as C
D=C.defaultdict
l,g,t=D(int),D(set),-1
for a,b in(re.findall(r'\b\w\b',x)for x in open("input.txt")):g[a]|={b};l[a]+=0;l[b]+=1
w,l[0]=5*[(0,0)],1
while t<0 or any(j for j,d in w):
 t+=1
 for i in range(5):
  j,d=w[i]
  if j and t>=d:
   for x in g[j]:l[x]-=1
   j=0
  if j<1:
   c,k=min(sorted((c,x)for x,c in l.items()))
   if not c:j,d=k,t+ord(k)-4;del l[j]
  w[i]=j,d
print t-1
