#if 0
cc -O3 $0;exec ./a.out
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define V struct V
V{long v;V*n;}*F,*L[9999],O[9999],*x;long s,i,j,r=10,m=1,N,S=sizeof(V);FILE*f;char l[9];
#define I f=fopen("input.txt","r");x=F=O+1;N=0;while(fgets(l,9,f)){x[-1].n=x;x->n=0;x->v=atol(l)*m;L[N]=x;++N,++x;}
#define R for(x=F;x;x=x->n){for(i=0;L[i]!=x;++i);memmove(L+i,L+i+1,(N-i-1)*S);i=(i+x->v)%(N-1);if(i<0)i+=N-1;memmove(L+i+1,L+i,(N-i-1)*S);L[i]=x;}
#define E for(i=0;L[i]->v;++i);s=0;for(j=3;j;--j){i+=1000;s+=L[i%N]->v;}printf("%ld\n",s)
int main(){I;R;E;m=811589153;I;while(r--){R;}E;return 0;}
