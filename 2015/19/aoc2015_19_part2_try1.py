import re,sys
I=list(open("input.txt"))
R=[map(str.strip,l.split('=>'))for l in I if'='in l]
def C(x,d):
 if'e'==x:print d;sys.exit()
 for n,o in R:[C(x[:m.start(0)]+n+x[m.end(0):],d+1)for m in re.finditer(o,x)]
C(max(I,key=len).strip(),0)
