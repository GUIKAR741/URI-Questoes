#include <stdio.h>
#define QTD 20
int main() {
    int x[QTD], i,j=0,aux;
    for(i=0;i<QTD;i++){
        scanf("%i",&x[i]);
    }
    for(i=QTD-1;i>=QTD/2;i--){
        aux=x[i];
        x[i]=x[j];
        x[j++]=aux;
    }
    for(i=0;i<QTD;i++){
        printf("N[%d] = %d\n",i,x[i]);
    }
    return 0;
}