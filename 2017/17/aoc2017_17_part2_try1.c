#if 0
cc -O9 $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#include <string.h>
#define N 345
#define M 50000000
typedef struct S{int v;struct S*n;}S;
S r[M+1];
main(){int x,i;S*n=r,*p=r;p->n=p;
for(x=1;x<=M;++x){for(i=N;i;--i)p=p->n;
(++n)->v=x;n->n=p->n;p->n=n;p=n;}
printf("%d\n",r[0].n->v);}
