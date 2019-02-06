b=[set()for x in range(500)]
c,r={},0
P=lambda i:int(w[i+1])-99*(w[i]>'o')
for l in open("input.txt"):
 w=l.split();j=int(w[1])
 if'c'<w[0]:b[int(w[5])]|={j}
 else:c[j]=(P(5),P(10))
while r<1:
 for i,n in enumerate(b[:-99]):
  if len(n)>1:x,y=sorted(n);b[i]=set();s,t=c[i];b[s]|={x};b[t]|={y}
 x,y,z=map(sum,b[-99:-96]);r=x*y*z
print r
