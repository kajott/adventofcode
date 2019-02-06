import re
t,D=0,[map(int,re.findall('\d+',l))for l in open("input.txt")]
while any((n+p+t)%m for n,m,x,p in D):t+=1
print t
