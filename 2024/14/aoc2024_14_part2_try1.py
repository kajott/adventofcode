W,H=101,103
import re;N=[[*map(int,re.findall(r'-?\d+',l))]for l in open("input.txt")]
p=[t:=-1,t]
while len(p)-len({*p}):t+=1;p=[((x+t*u)%W,(y+t*v)%H)for x,y,u,v in N]
print(t)
