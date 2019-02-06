R=[map(int,l.split('-'))for l in open("input.txt")]
v,x=0,[min(R)[1]]
while x:v=max(x)+1;x=[b for a,b in R if a<=v<=b]
print v
