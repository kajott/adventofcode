A,B=map(int,open("input.txt"))
i,j,X,M=1,1,0,20201227
while i!=A:i=(i*7)%M;X+=1
for k in range(X):j=(j*B)%M
print j
