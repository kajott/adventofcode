#if 0
cc $0||exit 1
exec ./a.out
#endif
#include <stdio.h>
#include <string.h>
#define N "640441"
char d[99999999],*r,*f,s;int l=2,a=0,b=1;
main(){r=strcpy(d,"---------37")+9;do{
s=r[a]+r[b]-96;if(s>9)r[l++]='1';r[l++]=48+s%10;
a=(a+r[a]-47)%l;b=(b+r[b]-47)%l;
f=strstr(&r[l-9],N);}while(!f);
printf("%d\n",f-r);}
