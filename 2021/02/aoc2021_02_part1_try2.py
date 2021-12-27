x=y=0
for l in open("input.txt"):
 n=int(l.split()[1])
 if'n'<l[3]:x+=n
 else:y+=n-2*n*(l>'f')
print x*y
