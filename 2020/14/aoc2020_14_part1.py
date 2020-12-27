M={}
for k,v in(map(str.strip,r.split('='))for r in open("input.txt")):
 if"me"<k:M[int(k[4:-1])]=int(v)&A|O
 else:A,O=(int(v.replace('X',d),2)for d in"10")
print sum(M.values())
