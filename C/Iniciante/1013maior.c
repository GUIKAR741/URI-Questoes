#include <stdio.h>
#include <math.h>
int main() {
    int A,B,C;
    double maior;
    scanf("%i %i %i",&A,&B,&C);
    maior=(A+B+fabs(A-B))/2;
    maior=(maior+C+fabs(maior-C))/2;
    printf("%.0lf eh o maior\n",maior);
    return 0;
}