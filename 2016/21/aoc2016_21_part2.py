d=list("fbgdceah");I=list.index;_=int
P=lambda:(_(w[2]),_(w[-1]))
for w in[l.strip().split()for l in open("input.txt")][::-1]:
 c,e=w[0][0],w[1][0]
 if'r'<c:a,b=P()if'l'<e else(I(d,w[2]),I(d,w[5]));d[a],d[b]=d[b],d[a]
 elif'r'>c:b,a=P();x=d.pop(a);d[b:b]=[x]
 elif'p'==e:a,b=P();d=d[:a]+d[a:b+1][::-1]+d[b+1:]
 else:
  if'l'>e:a=_("11627304"[I(d,w[6])])
  else:a=_(w[2])*(2*(e>'l')-1)
  d=d[a:]+d[:a]
print''.join(d)
