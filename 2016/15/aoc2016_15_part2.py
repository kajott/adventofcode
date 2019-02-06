import re
t,D=0,[map(int,re.findall('\d+',l))for l in open("input.txt")]
D+=[(len(D)+1,11,0,0)]
while any((n+p+t)%m for n,m,x,p in D):t+=1
print t
