N=361527
d=1;N-=2
while N>=d*8:N-=d*8;d+=1
print d+abs(N%(2*d)-d+1)
