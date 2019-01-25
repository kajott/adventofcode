A=str.isalpha
P=[l.strip().split()for l in open("input.txt")]
T=dict(zip("cjidt",("jnz","cpy","dec","inc","inc")))
r,i={'a':6,'b':0,'c':0,'d':0},0
G=lambda n:r[n]if A(n)else int(n)
t=0
while i<len(P):
 c=P[i];o=c[0][0];a=c[1];i+=1;t+=1
 print "%8d: [%02d] %-3s %3s %3s  " % (t, i-1, c[0], c[1], c[2] if len(c)>2 else ""),
 if'c'==o:r[c[2]]=G(a)
 if'i'==o:r[a]+=1
 if'd'==o:r[a]-=1
 if'j'==o and G(a):i+=G(c[2])-1
 if't'==o:
  j=i-1+r[a]
  if j<len(P):P[j][0]=T[P[j][0][0]]
 print "[ %8d, %8d, %8d, %8d]" % (r['a'], r['b'], r['c'], r['d'])
print r['a']
