A=1
for t,d in zip(*(map(int,l.split()[1:])for l in open("input.txt"))):A*=sum(d<h*(t-h)for h in range(t))
print(A)
