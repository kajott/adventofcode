N=3014603
e=[N-i for i in range(N)];l=N-1
while l:
 for i in range(l,-1,-1):e[i-1]*=e[i]<1
 e=filter(None,e);l=len(e)-1
print e[0]
