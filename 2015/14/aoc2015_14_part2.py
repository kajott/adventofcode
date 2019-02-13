R=[[int(l.split()[i])for i in(3,6,13)]for l in open("input.txt")]
S=[0]*len(R)
for t in range(1,2504):p=[s*(t/(f+r)*f+min(f,t%(f+r)))for s,f,r in R];m=max(p);S=[o+(q==m)for q,o in zip(p,S)]
print max(S)
