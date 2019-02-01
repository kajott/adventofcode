from hashlib import*
k,i=[0]*16,0
while not all(k[:8]):
 h=md5("cxdnnyjw"+str(i)).hexdigest();i+=1;p=int(h[5],16)
 if k[p]<1and"00000"==h[:5]:k[p]=h[6]
print''.join(k[:8])
