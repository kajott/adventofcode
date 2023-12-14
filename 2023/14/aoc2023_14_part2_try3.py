M=[*map(str.strip,open("input.txt"))];H,L=[],len(M)
while(M in H)-1:
 H+=[M]
 for _ in"NWSE":
  M=[''.join(c)for c in zip(*M[::-1])]
  for i in range(L):
   while"O."in M[i]:M[i]=M[i].replace("O.",".O")
t=len(H);p=t-H.index(M);print(sum(H[(int(1E9)-t)%p-p][i].count('O')*(L-i)for i in range(L)))
