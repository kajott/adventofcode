A=0
for l in open("input.txt"):
 n=[[*map(int,l.split())]]
 while any(n[-1]):n+=[[b-a for a,b in zip(n[-1],n[-1][1:])]]
 A+=sum(s[-1]for s in n)
print(A)
