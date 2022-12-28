E=enumerate
M,D,N=0,[1,-1j,1j,-1],set()
for y,l in E(open("input.txt")):N|={x+y*1j for x,c in E(l)if'#'==c}
for t in range(10):
 M,N,G=N,set(),{};D+=[D.pop(0)]
 for p in M:c=[p+d for d in D if any(p+d*n in M for n in(1,1+1j,1-1j))-1];n=c[0]if 0<len(c)<4else p;G[n]=G.get(n,set())|{p}
 for p in G:N|={p}if len(G[p])<2else G[p]
X={p.real for p in N};Y={p.imag for p in N}
print int((max(Y)-min(Y)+1)*(max(X)-min(X)+1))-len(N)
