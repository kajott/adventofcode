import re
A=str.isalpha
P=[re.match('(\w+) (\w) ?(-?\w+)?',l).groups()for l in open("input.txt")]
r,i,m={x:0for x in"abcdefgh"},0,0
while 0<=i<len(P):
 o,x,y=P[i];y=y and(r[y]if A(y)else int(y));v=r[x]if A(x)else int(x)
 if"set"==o:v=y
 if"sub"==o:v-=y
 if"mul"==o:v*=y;m+=1
 if"jnz"==o and v:i+=y-1
 r[x]=v;i+=1
print m
