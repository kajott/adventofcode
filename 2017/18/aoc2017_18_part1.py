import re
P=[re.match('(\w+) (\w) ?(-?\w+)?',l).groups()for l in open("input.txt")]
r,i={chr(x):0for x in range(97,123)},0
while 0<=i<len(P):
 o,x,y=P[i];y=y and(r[y]if y.isalpha()else int(y));v=r[x]
 if"snd"==o:f=v
 if"set"==o:v=y
 if"add"==o:v+=y
 if"mul"==o:v*=y
 if"mod"==o:v%=y
 if"rcv"==o and v:break
 if"jgz"==o and v>0:i+=y-1
 r[x]=v;i+=1
print f
