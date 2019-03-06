#include <stdio.h>
int main() {
    int a,b;
    double pagar;
    scanf("%d%d",&a,&b);
    if(a==1) pagar=b*4;
    if(a==2) pagar=b*4.5;
    if(a==3) pagar=b*5;
    if(a==4) pagar=b*2;
    if(a==5) pagar=b*1.5;
    printf("Total: R$ %.2lf\n",pagar);
    return 0;
}