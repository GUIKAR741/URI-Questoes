#include <stdio.h>
#include <math.h>
int main() {
    double salario,reajuste;
    scanf("%lf",&salario);
    if(salario>=0 && salario<=400){
        reajuste=salario*0.15;
        printf("Novo salario: %.2lf\n"
               "Reajuste ganho: %.2lf\n"
               "Em percentual: 15 %%\n",salario+reajuste,reajuste);
    }else if(salario>400 && salario<=800){
        reajuste=salario*0.12;
        printf("Novo salario: %.2lf\n"
               "Reajuste ganho: %.2lf\n"
               "Em percentual: 12 %%\n",salario+reajuste,reajuste);
    }else if(salario>800 && salario<=1200){
        reajuste=salario*0.10;
        printf("Novo salario: %.2lf\n"
               "Reajuste ganho: %.2lf\n"
               "Em percentual: 10 %%\n",salario+reajuste,reajuste);
    }else if(salario>1200 && salario<=2000){
        reajuste=salario*0.07;
        printf("Novo salario: %.2lf\n"
               "Reajuste ganho: %.2lf\n"
               "Em percentual: 7 %%\n",salario+reajuste,reajuste);
    }else if(salario>2000){
        reajuste=salario*0.04;
        printf("Novo salario: %.2lf\n"
               "Reajuste ganho: %.2lf\n"
               "Em percentual: 4 %%\n",salario+reajuste,reajuste);
    }
    return 0;
}