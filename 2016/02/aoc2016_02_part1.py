T,p,r={'U':"123123456",'D':"456789789",'L':"112445778",'R':"233566899"},5,""
for l in open("input.txt"):
 for c in l.strip():p=int(T[c][p-1])
 r+=str(p)
print r
