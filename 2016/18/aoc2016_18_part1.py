r,s=[c<'^'for c in open("input.txt").read().strip()]+[1],0
for y in range(40):s+=sum(r)-1;r=[r[i-1]^r[i+1]^1for i in range(len(r)-1)]+[1]
print s
