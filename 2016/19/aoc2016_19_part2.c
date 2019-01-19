#if 0
cc $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#define N 3014603
struct X{int i;struct X*n;} a[N],*p=a,*h=&a[N/2-1];
main(){int i,j;
for(i=1;i<N;++i){a[i].i=i;a[i-1].n=&a[i];}a[N-1].n=a;
for(i=N;i>1;--i){h->n=h->n->n;if(i&1)h=h->n;p=p->n;}
printf("%d\n",p->i+1);}
