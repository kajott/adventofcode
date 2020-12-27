#if 0
cc $0;exec ./a.out
#endif
#include <stdio.h>
#define N 30000000
int S[]={6,4,12,1,20,0,16},D[N];
int main(){int n,i,t;for(t=0;t<N;++t){n=t<sizeof(S)/sizeof(*S)?S[t]:!i?0:t-i;i=D[n];D[n]=t+1;}return!printf("%d\n",n);}
