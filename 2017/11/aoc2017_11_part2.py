x,m=0,0
for d in({"n":-2,"s":2,"nw":-1-1j,"ne":1j-1,"sw":1-1j,"se":1+1j}[x]for x in open("input.txt").read().strip().split(',')):x+=d;a,b=abs(x.imag),abs(x.real);m=max(m,int(a+(b-a)/2))
print m
