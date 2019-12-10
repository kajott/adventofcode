from fractions import*
A,S,E=set(),lambda x:1-2*(x<0),enumerate
for y,l in E(open("input.txt")):A|={x+y*1j for x,c in E(l)if'#'==c}
def V(a):
 v,n=set(A)-{a},0
 while v:
  b=v.pop();d=b-a;x,y=d.real,d.imag
  if y:s=Fraction(abs(int(x)),abs(int(y)));d=s.numerator*S(x)+s.denominator*S(y)*1j
  else:d=S(x)
  v-={a+i*d for i in range(36)};n+=1
 return n
print max(map(V,A))
