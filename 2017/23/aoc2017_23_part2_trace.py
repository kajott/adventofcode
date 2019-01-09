import re
A=str.isalpha
P=[re.match('(\w+) (\w) ?(-?\w+)?',l).groups()for l in open("input.txt")]
r,i={x:0for x in "abcdefgh"},0
r['a']=1;t=0
while 0<=i<len(P):
 o,x,y=P[i]
 print "%10d: [%02d] %s %s %-7s |"%(t,i,o,x,y),
 y=y and(r[y]if A(y)else int(y));v=r[x]if A(x)else int(x)
 if"set"==o:v=y
 if"sub"==o:v-=y
 if"mul"==o:v*=y
 if"jnz"==o and v:i+=y-1
 r[x]=v;i+=1;t+=1
 print' '.join("%8d"%r[x]for x in "abcdefgh")
print r['h']
