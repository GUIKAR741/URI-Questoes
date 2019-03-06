#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
    int a,i=0,r1,r2;
    scanf("%d",&a);
    while(i++<a){
        scanf("%d%d",&r1,&r2);
        printf("%d\n",(r1+r2));
    };
    return 0;
}