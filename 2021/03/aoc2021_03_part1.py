x=sum((sum(c)*2>len(c))<<(11-i)for i,c in enumerate(zip(*(map(int,l[:12])for l in open("input.txt")))))
print(x^4095)*x
