import re;N=[[*map(int,re.findall(r'-?\d+',l))]for l in open("input.txt")]
C=lambda x,y:sum((((p+100*u)%101-50)*x<0)*(((q+100*v)%103-51)*y<0)for p,q,u,v in N)
print(C(1,1)*C(-1,1)*C(1,-1)*C(-1,-1))
