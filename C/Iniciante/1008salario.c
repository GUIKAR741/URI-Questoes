#include <stdio.h>
int main() {
    int numero,horas;
    float recebehora,salario;
    scanf("%d %d %f",&numero,&horas,&recebehora);
    salario=recebehora*horas;
    printf("NUMBER = %i\nSALARY = U$ %.2f\n",numero,salario);
    return 0;
}