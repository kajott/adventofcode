import fractions as F,cmath as C,sys,time
A,L,D,E,R=set(),sys.stdout,{-1j},enumerate,range(1,36)
def B(p,c):L.write("\x1b[%d;%dH%s\x1b[37;1H"%(p.imag+1,p.real*2+1,c));L.flush()
for y,l in E(open("input.txt")):A|={x+y*1j for x,c in E(l)if'#'==c}
for x in R:D|={f.numerator-f.denominator*1j for f in(F.Fraction(x,y)for y in R)}
D=sorted(D,key=C.phase);D+=[d*1j for d in D];D+=[-d for d in D];L.write("\x1b[2J")
def V(a):
 B(a,'#');v,n=set(A)-{a},0
 for d in D:m=v&{a+i*d for i in R};v-=m;n+=bool(m)
 return n
d,x,y=max((V(a),a.real,a.imag)for a in A);a=x+y*1j;B(a,'X');A-={a}
while A:
 for d in D:
  m=A&{a+i*d for i in R}
  if m:b=min(m,key=lambda b:abs(b-a));A-={b};B(b,'*');time.sleep(0.05);B(b,' ')
