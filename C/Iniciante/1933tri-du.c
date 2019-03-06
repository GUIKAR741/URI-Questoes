#include <stdio.h>
int main(){
    int a,b, r = 0;
    scanf("%d%d",&a,&b);
    if(a==b){
        r=a;
    }
    if(a>b){
        r=a;
    }else{
        r=b;
    }
    printf("%d\n",r);
    return 0;
}