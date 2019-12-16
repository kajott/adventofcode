S=map(int,open("input.txt").read().strip())
R=range(1,len(S)+1)
M=[[((x/p)&1)*(1-((x/p)&2))for x in R]for p in R]
for i in range(100):S=[abs(sum(x*y for x,y in zip(r,S)))%10for r in M]
print''.join(map(str,S[:8]))
