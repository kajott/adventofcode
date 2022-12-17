import re;A,S=abs,set
B=S();H=S();Y=2000000
for x,y,u,v in(map(int,re.findall('-?\d+',l))for l in open("input.txt")):w=A(x-u)+A(y-v)-A(y-Y);B|=S([u]*(v==Y));H|=S(range(x-w,x+w+1))
print len(H)-len(B)
