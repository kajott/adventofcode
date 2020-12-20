N=map(int,open("input.txt"))
for i in range(25,len(N)):
 p=N[i-25:i];v={-1}
 for a in p:v|={a+b for b in p if a!=b}
 if not N[i]in v:print N[i]
