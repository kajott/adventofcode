G,R,S=[],{},[]
for l in open("input.txt"):
 if'>'in l:
  a,o,b,_,d=l.split();i=a,b;G+=[g:=(i,d,o[0])];R[d]=R.get(d,[])
  for j in i:R[j]=R.get(j,[])+[g]
for i,d,o in G:r={c[2]for c in R[d]};S+=[d]*(('O'>o)*(r!={'O'})*('00'<i[0][1:])+('O'<o)*(d[0]<'z')*(r!={*'AX'})+('O'==o)*(d>'z')*any(w>d for w in R))+[e for _,e,p in R[d]if('O'<p)*(e<'z')]*('O'<o)*all(j>'x'for j in i)
print(','.join(sorted({*S})))
