j,p,s=[int(x.strip())for x in open("input.txt")],0,0
while 0<=p<len(j):s+=1;j[p]+=1;p+=j[p]-1
print s
