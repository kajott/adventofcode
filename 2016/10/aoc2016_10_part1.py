b=[set()for x in range(500)]
c,r={},-1
P=lambda i:int(w[i+1])-99*(w[i]>'o')
for l in open("input.txt"):
 w=l.split();j=int(w[1])
 if'c'<w[0]:b[int(w[5])]|={j}
 else:c[j]=(P(5),P(10))
while r<0:
 for i,n in enumerate(b[:-1]):
  if{17,61}==n:r=i
  if len(n)>1:x,y=sorted(n);b[i]=set();s,t=c[i];b[s]|={x};b[t]|={y}
print r
