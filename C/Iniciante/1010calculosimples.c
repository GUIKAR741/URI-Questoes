#include <stdio.h>
int main(){
    float codigo1 , numeropecas1 ,valorpecas1,codigo2 , numeropecas2 ,valorpecas2,VALOR;
    scanf("%f%f%f", &codigo1, &numeropecas1, &valorpecas1);
    scanf("%f%f%f", &codigo2, &numeropecas2, &valorpecas2);
    VALOR=valorpecas1*numeropecas1+numeropecas2*valorpecas2;
    printf("VALOR A PAGAR: R$ %.2lf\n",VALOR);
    return 0;
}