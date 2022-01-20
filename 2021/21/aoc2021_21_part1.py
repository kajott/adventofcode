import re
F=[int(x)-1for x in re.findall('\d+',open("input.txt").read())[1::2]]
S=[0,0];D=p=0
while max(S)<1000:f=(F[p]+D%100+(D+1)%100+(D+2)%100+3)%10;F[p]=f;S[p]+=f+1;p^=1;D+=3
print min(S)*D
