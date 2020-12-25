t,d=0,1
for i,n in[(i,int(n))for i,n in enumerate(list(open("input.txt"))[-1].split(','))if'x'>n]:
 while t%n!=(-i)%n:t+=d
 d*=n
print t
