d=map(int,"10010000000110000")
while len(d)<272:d+=[0]+[x^1for x in d[::-1]]
d=d[:272]
while len(d)&1<1:d=[d[i]^d[i+1]^1for i in range(0,len(d),2)]
print''.join(map(str,d))
