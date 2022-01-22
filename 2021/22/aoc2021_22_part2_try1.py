import re
R,G=range,set()
C=[map(int,re.findall('-?\d+',l))+[l]for l in open("input.txt")]
X,Y,Z=[sorted([z[i]for z in C]+[z[i+1]+1for z in C])for i in(0,2,4)]
U=X.index;V=Y.index;W=Z.index
for a,b,c,d,e,f,l in C:
 u={(x,y,z)for x in R(U(a),U(b+1))for y in R(V(c),V(d+1))for z in R(W(e),W(f+1))}
 if'f'<l[1]:G|=u
 else:G-=u
print sum((X[x+1]-X[x])*(Y[y+1]-Y[y])*(Z[z+1]-Z[z])for x,y,z in G)
