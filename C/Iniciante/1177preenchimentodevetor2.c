#include <stdio.h>
#define QTD 1000
int main() {
    int x[QTD],i,v,j=0;
    scanf("%d",&v);
    for(i=0;i<QTD;i++){
        if(j>=v)j=0;
        x[i]=j;
        j++;
    }
    for(i=0;i<QTD;i++){
        printf("N[%d] = %d\n",i,x[i]);
    }
    return 0;
}