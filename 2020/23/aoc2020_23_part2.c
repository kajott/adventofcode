#if 0
cc $0;exec ./a.out
#endif
#include <stdio.h>
char *I="463528179:";
#define N 1000000
int M[N+1],t,p,a,b,c,d,n;int main(){
for(t=0;t<9;++t)M[I[t]-'0']=I[t+1]-'0';for(t=10;t<N;++t)M[t]=t+1;M[N]=p=I[0]-'0';
for(t=10*N;t;--t){
a=M[p];b=M[a];c=M[b];n=M[c];d=p;
do d=(d>1)?(d-1):N;while (d==a||d==b||d==c);
M[c]=M[d];M[d]=a;M[p]=n;p=n;}
return!printf("%ld\n",(long)M[1]*(long)M[M[1]]);}
