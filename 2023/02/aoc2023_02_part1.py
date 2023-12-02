A,S,C=0,str.split,{"r":12,"g":13,"b":14}
for l in open("input.txt"):
 i,l=S(l,':');k=1
 for c in S(l.replace(';',','),','):n,c=S(c);k*=int(n)<=C[c[0]]
 A+=int(S(i)[1])*k
print(A)
