import re;N=[[*map(int,re.findall(r'-?\d+',l))]for l in open("input.txt")]
W,H=M=[101,103]
def V(c,t):a=sum(p:=[(k[c]+k[c+2]*t)%M[c]for k in N])/len(p);return sum(abs(x-a)for x in p),t
x,y=(min(V(c,t)for t in range(M[c]))[1]for c in(0,1))
while x%H-y:x+=W
print(x)
