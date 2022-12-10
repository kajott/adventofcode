P=[];v=1
for L in open("input.txt"):
 P+=[v]
 if'n'>L:v+=int(L.split()[1]);P+=[v]
print sum(i*P[i-2]for i in range(20,240,40))
