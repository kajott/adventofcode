import re
A=str.isalpha
P=[re.match('(\w+) (\w) ?(-?\w+)?',l).groups()for l in open("input.txt")]
s=[[{chr(x):0for x in range(97,123)},0,[],0]for i in"01"]
s[1][0]['p']=1;a=z=0
while z<2:
 a=1-a;r,i,q,c=s[a]
 if not(0<=i<len(P)and(P[i][0]!="rcv"or q)):z+=1;continue
 z=0;o,x,y=P[i];y=y and(r[y]if A(y)else int(y));v=r[x]if A(x)else int(x)
 if"snd"==o:s[1-a][2]+=[v];s[a][3]+=1
 if"set"==o:v=y
 if"add"==o:v+=y
 if"mul"==o:v*=y
 if"mod"==o:v%=y
 if"rcv"==o:
  if q:v=q.pop(0)
  else:i-=1
 if"jgz"==o and v>0:i+=y-1
 r[x]=v;s[a][1]=i+1
print s[1][3]
