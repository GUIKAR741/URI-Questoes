#include <stdio.h>
int main(){
    int a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    if ((a+b)>c && (a+c)>b && (b+c)>a){
        printf("S\n");
    } else if ((a+b)>d && (a+d)>b && (b+d)>a){
        printf("S\n");
    } else if ((d+b)>c && (d+c)>b && (b+c)>d){
        printf("S\n");
    } else if ((d+a)>c && (d+c)>a && (a+c)>d){
        printf("S\n");
    }else{
        printf("N\n");
    }
    return 0;
}