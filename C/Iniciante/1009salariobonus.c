#include <stdio.h>
#include <string.h>
int main() {
    char vendedor[20];
    double salario,vendas,receber;
    gets(vendedor);
    scanf("%lf %lf",&salario,&vendas);
    receber=salario+(vendas*0.15);
    printf("TOTAL = R$ %.2lf\n",receber);
    return 0;
}