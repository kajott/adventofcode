E,A=enumerate,0
B=sorted(([*map(int,l.replace('~',',').split(','))]for l in open("input.txt")),key=lambda b:b[2])
O,S,R=({i:set()for i,b in E(B)}for x in"AoC")
for i,a in E(B):
 for j,b in E(B[:i]):
  if(min(a[3],b[3])>=max(a[0],b[0]))*(min(a[4],b[4])>=max(a[1],b[1])):O[i]|={j};O[j]|={i}
for i,a in E(B):z=max([B[j][5]for j in O[i]if j<i]or[0])+1;a[5]+=z-a[2];a[2]=z
for i,a in E(B):
 for j in O[i]:
  if B[j][2]==B[i][5]+1:S[i]|={j};R[j]|={i}
for i,a in E(B):
 e={i};f={i}
 while e:f|=e;e={j for i in e for j in S[i]if R[j]<=f}
 A+=len(f)-1
print(A)
