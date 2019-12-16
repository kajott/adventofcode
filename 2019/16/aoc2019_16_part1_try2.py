S=map(int,open("input.txt").read().strip())
R=range(1,len(S)+1)
for i in range(100):S=[abs(sum(y*((x/p)&1)*(1-((x/p)&2))for x,y in zip(R,S)))%10for p in R]
print''.join(map(str,S[:8]))
