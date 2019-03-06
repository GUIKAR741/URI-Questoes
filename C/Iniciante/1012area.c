#include <stdio.h>
#include <math.h>
int main() {
    double A,B,C,pi=3.14159,triangulo,circulo,trapezio,quadrado,retangulo;
    scanf("%lf %lf %lf",&A,&B,&C);
    triangulo=(A*C)/2;
    circulo=pow(C,2)*pi;
    trapezio=((A+B)/2)*C;
    quadrado=pow(B,2);
    retangulo=A*B;
    printf("TRIANGULO: %.3f\n"
           "CIRCULO: %.3f\n"
           "TRAPEZIO: %.3f\n"
           "QUADRADO: %.3f\n"
           "RETANGULO: %.3f\n",triangulo,circulo,trapezio,quadrado,retangulo);
    return 0;
}