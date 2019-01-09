import re
N=int(re.findall('\d+',open("input.txt").read())[0])*100+10**5
print sum(any((b%m)==0for m in range(2,b/2+1))for b in range(N,N+17001,17))
