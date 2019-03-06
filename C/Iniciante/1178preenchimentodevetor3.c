#include <stdio.h>
#define QTD 100
int main() {
    int i;
    double v,x[QTD];
    scanf("%lf",&v);
    x[0]=v;
    for(i=1;i<QTD;i++){
        x[i]=x[i-1]/2;
    }
    for(i=0;i<QTD;i++){
        printf("N[%d] = %.4lf\n",i,x[i]);
    }
    return 0;
}