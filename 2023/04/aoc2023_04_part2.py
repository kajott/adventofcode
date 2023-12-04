C,i,S,A={},0,str.split,0
for l in open("input.txt"):
 w,h=({*S(x)}for x in S(S(l,':')[1],'|'));n=C.get(i,1);A+=n;i+=1
 for j in range(i,i+len(w&h)):C[j]=C.get(j,1)+n
print(A)
