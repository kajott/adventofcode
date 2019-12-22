N=10007;S=range(N)
for l in open("input.txt"):
 w=l.split()
 if'c'==l[0]:n=int(w[-1]);S=S[n:]+S[:n]
 elif'w'==l[5]:
  n=int(w[-1]);x=S[:];j=0
  for v in x:S[j]=v;j=(j+n)%N
 else:S=S[::-1]
print S.index(2019)
