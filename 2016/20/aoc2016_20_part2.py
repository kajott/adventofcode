p,s,R=0,0,[map(int,l.split('-'))for l in open("input.txt")]
while p<1<<32:
 x=[b for a,b in R if a<=p<=b]
 if x:p=max(x)+1
 else:q=min(a for a,b in R if a>p);s+=q-p;p=q+1
print s
