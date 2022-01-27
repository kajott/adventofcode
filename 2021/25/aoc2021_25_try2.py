G=[[".1234>v".index(c)for c in l.strip()]for l in open("input.txt")]
R,t=[(x,y)for x in range(len(G[0]))for y in range(len(G))],0
M=lambda m:[[x&m for x in r]for r in G]
while sum(map(sum,M(4))):
 G=M(3);t+=1
 for x,y in R:
  if(G[y][x]<1)*(G[y][x-1]==1):G[y][x]=5;G[y][x-1]=8
 G=M(7)
 for x,y in R:
  if(G[y][x]<1)*(G[y-1][x]==2):G[y][x]=6;G[y-1][x]=8
print t
