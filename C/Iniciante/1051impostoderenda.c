#include <stdio.h>
int main() {
    double salario;
    scanf("%lf",&salario);
    if(salario>=0 && salario<=2000){
        printf("Isento\n");
    }
    if(salario>2000 && salario<=3000){
        salario-=2000;
        printf("R$ %.2lf\n",(salario*0.08));
    }
    if(salario>3000 && salario<=4500){
        salario-=3000;
        printf("R$ %.2lf\n",((1000*0.08)+(salario*0.18)));
    }
    if(salario>4500){
        salario-=4500;
        printf("R$ %.2lf\n",((1000*0.08)+(1500*0.18)+(salario*0.28)));
    }
    return 0;
}