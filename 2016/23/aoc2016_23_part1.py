A=str.isalpha
P=[l.strip().split()for l in open("input.txt")]
T=dict(zip("cjidt","jcdii"))
r,i={'a':7,'b':0,'c':0,'d':0},0
G=lambda n:r[n]if A(n)else int(n)
while i<len(P):
 c=P[i];o=c[0][0];a=c[1];i+=1
 if'c'==o:r[c[2]]=G(a)
 if'i'==o:r[a]+=1
 if'd'==o:r[a]-=1
 if'j'==o and G(a):i+=G(c[2])-1
 if't'==o:
  j=i-1+r[a]
  if j<len(P):P[j][0]=T[P[j][0][0]]
print r['a']
