import re;N=[[*map(int,re.findall(r'-?\d+',l))]for l in open("input.txt")]
W,H=M=[101,103]
def V(c,t):a=sum(p:=[(k[c]+k[c+2]*t)%M[c]for k in N])/len(p);return sum(abs(x-a)for x in p)
print(min((V(0,t)+V(1,t),t)for t in range(W*H))[1])
