#if 0
cc -O9 $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#include <stdlib.h>
struct{short g,p;}C[130321];int main(){int x,p,l,s,i,n=0,M=0xFFFFFF;long r=0;
FILE*f=fopen("input.txt","r");char z[42];while(fgets(z,42,f)){++n;x=atoi(z);p=x%10;s=0;
for(i=2000;i;--i){x^=x<<6;x&=M;x^=x>>5;x^=x<<11;x&=M;l=p;p=x%10;s=s%6859*19+9+p-l;if(C[s].g<n){C[s].g=n;C[s].p+=p;}}
r+=x;}n=0;for(i=130320;i;--i)if(C[i].p>n)n=C[i].p;printf("%ld\n%d\n",r,n);return 0;}
