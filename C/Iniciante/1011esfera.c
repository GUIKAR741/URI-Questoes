#include <stdio.h>
#include <math.h>
int main() {
    double pi=3.14159,raio,area;
    scanf("%lf",&raio);
    area=(4.0/3)*pow(raio,3)*pi;
    printf("VOLUME = %.3lf\n",area);
    return 0;
}