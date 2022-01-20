import re
a,b=map(int,re.findall('\d+',open("input.txt").read())[1::2])
D,C=zip(range(2,9),map(int,"1367631")),{}
def V(k):
 if k in C:return C[k]
 if max(k[3:])>20:return k[3]>20,k[4]>20
 a=b=0;p=k[2]
 for s,f in D:m=list(k);m[2]^=1;m[p]=(m[p]+s)%10+1;m[p+3]+=m[p];i,j=V(tuple(m));a+=f*i;b+=f*j
 C[k]=(a,b);return a,b
print max(*V((a,b,0,0,0)))
