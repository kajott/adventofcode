from hashlib import*
K="gdjjyniy"
c,q={""},set()
while c or q:
 if not c:c=q;q=set()
 p=c.pop();x=sum({'D':1j,'U':-1j,'L':-1,'R':1}[x]for x in p);x,y=x.real,x.imag
 if min(x,y)>2:r=len(p)
 else:q|={p+d for d,e,l in zip("UDLR",(y>0,y<3,x>0,x<3),md5(K+p).hexdigest())if('a'<l)*e}
print r
