I=map(int,open("input.txt").read().strip())
L=[I[x:x+150]for x in range(0,len(I),150)]
C=L[min((l.count(0),i)for i,l in enumerate(L))[1]]
print C.count(1)*C.count(2)
