#include <stdio.h>
int main(){
    int s,t,f,ret;
    scanf("%d%d%d",&s,&t,&f);
    ret=s+t+f;
    if(ret>=24)ret-=24;
    else if(ret<0)ret+=24;
    printf("%d\n",ret);
    return 0;
}