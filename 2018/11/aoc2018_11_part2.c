#if 0
cc -O4 $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#define S 7989
#define N 300
int g[N][N],p[N][N],x,y,s,a,b=0;
main(){
for(y=0;y<N;++y)for(x=0;x<N;++x)g[y][x]=((x+11)*(y+1)+S)*(x+11)/100%10-5;
for(s=0;s<=N;++s){
for(y=0;y<N;++y){a=0;for(x=0;x<N;++x){a+=g[y][x];if(x>=s){p[y][x-s]=a;a-=g[y][x-s];}}}
for(x=0;x<N-s;++x){a=0;for(y=0;y<N;++y){a+=p[y][x];if(y>=s){
if(a>b){b=a;printf("%d,%d,%d\n",x+1,y-s+1,s+1);}
a-=p[y-s][x];}}}}}
