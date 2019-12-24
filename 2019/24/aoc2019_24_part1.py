R=range(5)
N=[[c=='#'for c in l]+[0]for l in open("input.txt")]+[6*[0]]
H={-1};r=0
while{r}-H:
 H|={r};S=N;N=[6*[0]for y in R+[0]];r=0;b=1
 for y in R:
  for x in R:n=S[y-1][x]+S[y][x-1]+S[y+1][x]+S[y][x+1];n=n==1if S[y][x]else n in(1,2);N[y][x]=n;r|=b*n;b<<=1
print r
