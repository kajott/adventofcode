#if 0
cc $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#define P 403
#define N 7192000
struct X{long i;struct X *p,*n;};
struct X h[N];
long s[P],m=0;
main(){
struct X f={0,&f,&f},*c=&f;
for(long i=1;i<N;++i){
if(i%23){c=c->n;struct X *x=&h[i-1];x->i=i;x->p=c;x->n=c->n;x->p->n=x;x->n->p=x;c=x;}
else{long j=i%P;c=c->p->p->p->p->p->p->p;c->p->n=c->n;c->n->p=c->p;s[j]+=c->i+i;if(s[j]>m)m=s[j];c=c->n;}}
printf("%ld\n",m);}
