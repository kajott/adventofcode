N=345
b,p=[0],0
for x in range(1,2018):p=(p+N+1)%len(b);b[p:p]=[x]
print b[p+1]
