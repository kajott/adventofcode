E=enumerate
G,M=[(x,y)for y,r in E(open("input.txt"))for x,c in E(r)if'#'==c],[]
for d in(0,1):
 u=sorted({p[d]for p in G});p=u[0];M+=[{p:p}]
 for a,b in zip(u,u[1:]):p+=(b-a)*2-1;M[d][b]=p
X,Y=M;L=len(G);print(sum(abs(X[G[i][0]]-X[G[j][0]])+abs(Y[G[i][1]]-Y[G[j][1]])for i in range(L)for j in range(i,L)))
