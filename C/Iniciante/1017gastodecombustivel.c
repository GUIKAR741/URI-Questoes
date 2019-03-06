#include <stdio.h>
int main() {
    int horas,km;
    double kmh;
    scanf("%i %i",&horas,&km);
    kmh=(km*horas)/12.0;
    printf("%.3lf\n", kmh);
    return 0;
}