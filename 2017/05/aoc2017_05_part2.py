j,p,s=[int(x.strip())for x in open("input.txt")],0,0
while 0<=p<len(j):s+=1;i=j[p];j[p]+=1-2*(i>2);p+=i
print s
