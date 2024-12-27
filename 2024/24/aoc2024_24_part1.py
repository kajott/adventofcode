import operator as O
W,G={},[]
for l in open("input.txt"):
 s=l.split
 if':'in l:a,b=s(':');W[a]=int(b)
 if'>'in l:G+=[s()]
for _ in G:
 for a,o,b,_,d in G:W[d]={'A':O.and_,'O':O.or_,'X':O.xor}[o[0]](W.get(a,0),W.get(b,0))
print(sum(W[n]<<int(n[1:])for n in W if'z'<n))
