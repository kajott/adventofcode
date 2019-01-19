import re,sys
I=list(open("input.txt"))
R=sorted((map(str.strip,l.split('=>'))for l in I if'='in l),key=lambda x:len(x[0])-len(x[1]))
def C(x,d):
 if'e'==x:print d;sys.exit()
 for n,o in R:[C(x[:m.start(0)]+n+x[m.end(0):],d+1)for m in re.finditer(o,x)]
C(max(I,key=len).strip(),0)
