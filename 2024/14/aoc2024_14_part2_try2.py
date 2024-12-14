import re;N=[[*map(int,re.findall(r'-?\d+',l))]for l in open("input.txt")]
W,H,R=101,103,range
for t in R(W*H):
 m={((x+t*u)%W,(y+t*v)%H)for x,y,u,v in N}
 if 9*b'\1'in bytes((x,y)in m for y in R(H)for x in R(W)):print(t)
