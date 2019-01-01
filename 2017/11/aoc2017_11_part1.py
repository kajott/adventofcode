x=sum({"n":-2,"s":2,"nw":-1-1j,"ne":1j-1,"sw":1-1j,"se":1+1j}[x]for x in open("input.txt").read().strip().split(','))
a,b=abs(x.imag),abs(x.real)
print int(a+(b-a)/2)
