H,A,R=[[*map(int,l.replace('@',',').split(','))]for l in open("input.txt")],[],range
C=lambda x:[x[i]*x[j+3]-x[j]*x[i+3]for i,j in((1,2),(2,0),(0,1))]
while len(H)>2:
 M=[]
 for j in(1,2):a=[x-y for x,y in zip(H[0],H[j])];M+=[[a[(-l-k)%3+g]*((1-l+k)%3-1)for g in(0,3)for l in(0,1,2)]+[C(H[j])[k]-C(H[0])[k]]for k in(0,1,2)]
 for i in R(6):
  p=max(R(i,6),key=lambda j:abs(M[j][i]));M[p]=[x/M[p][i]for x in M[p]];M[i],M[p]=M[p],M[i]
  for j in R(i+1,6):M[j]=[x-y*M[j][i]for x,y in zip(M[j],M[i])]
 for i in(5,4,3):
  for j in R(i):M[j][i:]=[x-y*M[j][i]for x,y in zip(M[j][i:],M[i][i:])]
 A+=[sum(round(M[i][6])for i in(3,4,5))];del H[0]
print(max(A,key=lambda x:A.count(x)))
