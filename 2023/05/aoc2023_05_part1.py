M,A=[],[]
for l in open("input.txt"):
 p=l.split()
 if"s:"in l:S=[*map(int,p[1:])]
 elif":"in l:M+=[[]]
 elif"0"<l:M[-1]+=[[*map(int,p)]]
for n in S:
 for m in M:n=([n-s+d for d,s,l in m if s<=n<s+l]+[n])[0]
 A+=[n]
print(min(A))
