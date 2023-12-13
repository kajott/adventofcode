E,R=enumerate,range
def X(m):
 for i in R(len(m)-1,-1,-1):
  if all(c=='.'for c in m[i]):m[i:i]=[m[i]]
 return[*zip(*m)]
M=X(X([*map(str.strip,open("input.txt"))]))
G=[(x,y)for y,r in E(M)for x,c in E(r)if'#'==M[y][x]];L=len(G)
print(sum(abs(G[i][0]-G[j][0])+abs(G[i][1]-G[j][1])for i in R(L)for j in R(i,L)))
