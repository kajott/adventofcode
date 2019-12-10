import fractions as F,cmath as C
A,D,E,R=set(),{-1j},enumerate,range(1,36)
for y,l in E(open("input.txt")):A|={x+y*1j for x,c in E(l)if'#'==c}
for x in R:D|={f.numerator-f.denominator*1j for f in(F.Fraction(x,y)for y in R)}
D=sorted(D,key=C.phase);D+=[d*1j for d in D];D+=[-d for d in D]
def V(a):
 v,n=set(A)-{a},0
 for d in D:m=v&{a+i*d for i in R};v-=m;n+=bool(m)
 return n
d,x,y=max((V(a),a.real,a.imag)for a in A);a=x+y*1j;n=200
while n:
 for d in D:
  m=A&{a+i*d for i in R}
  if m:b=min(m,key=lambda b:abs(b-a));A-={b};n-=1
  if n<1:break
print int(b.real*100+b.imag)
