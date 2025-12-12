import re;S,T=[],0
for l in open("input.txt"):
 if'x'in l:w,h,*c=map(int,re.findall(r'\d+',l));T+=sum(n*s for n,s in zip(c,S))<=w*h
 elif':'in l:c=0
 else:c+=(a:=l.count('#'));S+=[c]*(a<1)
print(T)
