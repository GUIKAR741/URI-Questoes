#include <stdio.h>
#include <math.h>
int main() {
    double a,b,c;
    scanf("%lf%lf%lf",&a,&b,&c);
    if (a < c) {
        double tmp = c;
        c = a;
        a = tmp;
    }
    if (a < b) {
        double tmp = b;
        b = a;
        a = tmp;
    }
    if (b < c) {
        double tmp = c;
        c = b;
        b = tmp;
    }
    if(a>=b+c){
        printf("NAO FORMA TRIANGULO\n");
    }else {
        if (pow(a, 2) == pow(b, 2) + pow(c, 2)) {
            printf("TRIANGULO RETANGULO\n");
        }
        if (pow(a, 2) > pow(b, 2) + pow(c, 2)) {
            printf("TRIANGULO OBTUSANGULO\n");
        }
        if (pow(a, 2) < pow(b, 2) + pow(c, 2)) {
            printf("TRIANGULO ACUTANGULO\n");
        }
        if (a == b && b == c) {
            printf("TRIANGULO EQUILATERO\n");
        }
        if ((a == b && a != c) || (a == c && a != b) || (b==c && b!=a)) {
            printf("TRIANGULO ISOSCELES\n");
        }
    }
    return 0;
}