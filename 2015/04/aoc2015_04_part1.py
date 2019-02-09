from hashlib import*
n=0
while md5("ckczppom"+str(n)).hexdigest()[:5]>5*'0':n+=1
print n
