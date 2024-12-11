C=open("input.txt").read().split()
for t in range(25):
 p,C=C,[]
 for n in p:l=len(n);C+=['1']if n<'1'else[str(int(n)*2024)]if l&1 else[n[:l//2],str(int(n[l//2:],10))]
print(len(C))
