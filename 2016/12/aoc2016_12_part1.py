A=str.isalpha
P=[l.strip().split()for l in open("input.txt")]
r,i={x:0for x in"abcd"},0
while i<len(P):
 c=P[i];o=c[0][0];a=c[1];i+=1
 if'c'==o:r[c[2]]=r[a]if A(a)else int(a)
 if'i'==o:r[a]+=1
 if'd'==o:r[a]-=1
 if'j'==o and(not A(a)or r[a]):i+=int(c[2])-1
print r['a']
