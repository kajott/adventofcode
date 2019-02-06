#if 0
cc -O9 $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#include <string.h>
#define N 35651584
char d[N*2+1];
main(){strcpy(d,"10010000000110000");unsigned i,l=strlen(d);
while(l<N){d[l]='0';for(i=1;i<=l;++i)d[l+i]=d[l-i]^1;l=2*l+1;}
l=N;while(!(l&1)){for(i=0;i<l;i+=2)d[i/2]=d[i]^d[i+1]^'1';l/=2;}
d[l]='\0';puts(d);}
