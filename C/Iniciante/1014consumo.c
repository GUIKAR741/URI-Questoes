#include <stdio.h>
int main() {
    int km;
    double l,kml;
    scanf("%i %lf",&km,&l);
    kml=km/l;
    printf("%.3lf km/l\n",kml);
    return 0;
}