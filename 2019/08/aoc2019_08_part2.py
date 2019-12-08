I,N=map(int,open("input.txt").read().strip()),150;C=N*[0]
for L in(I[x:x+N]for x in range(0,len(I),N)):C=[c or 2-l for c,l in zip(C,L)]
for r in range(0,N,25):print''.join("?# "[x]for x in C[r:r+25])
