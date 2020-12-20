N=[0]+sorted(map(int,open("input.txt")))
P=[0,0,0,1]
for i in range(1,N[-1]+4):P+=[sum(N.count(i+k)*P[k]for k in(-3,-2,-1))]
print P[-1]
