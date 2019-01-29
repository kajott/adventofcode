d=list("abcdefgh");I=list.index
P=lambda:(int(w[2]),int(w[-1]))
for w in(l.strip().split()for l in open("input.txt")):
 c,e=w[0][0],w[1][0]
 if'r'<c:a,b=P()if'l'<e else(I(d,w[2]),I(d,w[5]));d[a],d[b]=d[b],d[a]
 elif'r'>c:a,b=P();x=d.pop(a);d[b:b]=[x]
 elif'p'==e:a,b=P();d=d[:a]+d[a:b+1][::-1]+d[b+1:]
 else:
  if'l'>e:a=I(d,w[6]);a=(7-a-a/4)&7
  else:a=int(w[2])*(1-2*(e>'l'))
  d=d[a:]+d[:a]
print''.join(d)
