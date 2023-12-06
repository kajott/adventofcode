M,N=[],min
for l in open("input.txt"):
 p=l.split()
 if"s:"in l:S=[*map(int,p[1:])]
 elif":"in l:M+=[[]]
 elif"0"<l:M[-1]+=[[*map(int,p)]]
r=[(s,s+l)for s,l in zip(S[::2],S[1::2])]
for m in M:
 m.sort(key=lambda x:x[1]);q,r=r,[]
 for a,b in q:
  for d,s,l in m:
   if(a<s+l)*(b>=s):
    if a<s:r+=[(a,N(b,s))];a=s
    if(a>=s)*(b>s):r+=[(a-s+d,N(b,s+l)-s+d)];a=N(b,s+l)
    if a>=b:break
  if b>a:r+=[(a,b)]
print(N(r)[0])
