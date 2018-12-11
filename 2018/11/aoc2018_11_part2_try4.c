#if 0
cc -O4 $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#define S 7989
#define N 300
int t[N+1][N+1],x,y,s,a,b=0;
main(){
for(y=1;y<=N;++y){a=0;for(x=1;x<=N;++x)t[y][x]=a+=((x+10)*y+S)*(x+10)/100%10-5+t[y-1][x]-t[y-1][x-1];}
for(s=1;s<=N;++s){
for(y=s;y<=N;++y)for(x=s;x<=N;++x){a=t[y][x]-t[y-s][x]-t[y][x-s]+t[y-s][x-s];
if(a>b){b=a;printf("%d,%d,%d\n",x-s+1,y-s+1,s);}}}}
