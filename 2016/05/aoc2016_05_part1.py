from hashlib import*
k,i="",0
while len(k)<8:
 h=md5("cxdnnyjw"+str(i)).hexdigest();i+=1
 if"00000"==h[:5]:k+=h[5]
print k
