import re,itertools as T
I=[[tuple(ord(c)-32for c in t[i:i+3])for i in range(0,len(t),3)]for t in["($ *% 9& H' j( ",'   - !? "U #k $\x86 %']+2*['   9! R" \x84# 4 !H "p #']]
H,D,A=map(int,re.findall('\d+',open("input.txt").read()))
print max(c for c,d,a in(map(sum,zip(*set(v)))for v in T.product(*I))if(H-1)/max(1,d-A)>99/max(1,D-a))
