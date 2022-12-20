#if 0
cc -O3 $0;exec ./a.out
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
long V[9999],O[9999],i,r,m=1,c=1,N,S=sizeof(i);FILE*f;char l[9];
#define P f=fopen("input.txt","r");for(N=0;fgets(l,9,f);++N){O[N]=N;V[N]=atol(l)*m;}\
for(r=0;r<N*c;++r){for(i=0;O[i]!=r%N;++i);m=V[O[i]];memmove(O+i,O+i+1,(N-i-1)*S);i=(i+m)%(N-1);if(i<0)i+=N-1;memmove(O+i+1,O+i,(N-i-1)*S);O[i]=r%N;}\
for(i=0;V[O[i]];++i);r=0;for(c=3;c;--c){i+=1000;r+=V[O[i%N]];}printf("%ld\n",r)
int main(){P;m=811589153;c=10;P;return 0;}
