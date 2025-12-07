for L in open("input.txt"):
 if'S'in L:B={L.index('S'):1}
 p,B=B,{}
 for x in p:
  for y in[x]if'Z'>L[x]else[x-1,x+1]:B[y]=B.get(y,0)+p[x]
print(sum(B.values()))
