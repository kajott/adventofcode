R,X=range,0
W=[set(R(x,x+5))for x in R(0,25,5)]+[set(R(x,25,5))for x in R(5)]
F=list(open("input.txt"))
B=[map(int,''.join(F[n:n+6]).split())+[{-1}]for n in range(1,len(F),6)]
for d in map(int,F[0].split(',')):
 for b in B:
  if d in b:b[-1]|={b.index(d)}
  if any(w<=b[-1]for w in W):X=X or d*sum(b[i]for i in R(25)if(i in b[-1])-1)
print X
