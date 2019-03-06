#include <stdio.h>
#define QTD 100
int main() {
    double x[QTD];
    int i;
    for(i=0;i<QTD;i++){
        scanf("%lf",&x[i]);
    }
    for(i=0;i<QTD;i++){
        if(x[i]<=10){
            printf("A[%d] = %.1lf\n",i,x[i]);
        }
    }
    return 0;
}