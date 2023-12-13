A=0
for l in open("input.txt"):
 n=[[*map(int,l.split())]]
 while any(n[-1]):n+=[[b-a for a,b in zip(n[-1],n[-1][1:])]]
 A+=sum(n[i][0]*(1-2*(i&1))for i in range(len(n)))
print(A)
