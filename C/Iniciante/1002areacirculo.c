#include <stdio.h>
#include <math.h>
int main() {
    double pi=3.14159,raio,area;
    scanf("%lf",&raio);
    area=pow(raio,2)*pi;
    printf("A=%.4lf\n",area);
    return 0;
}