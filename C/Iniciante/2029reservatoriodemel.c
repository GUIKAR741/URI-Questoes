#include <stdio.h>
#include <math.h>
int main(){
    double v,d,a,aa;
    while (scanf("%lf %lf",&v,&d)!=EOF){
        aa=pow((d/2),2)*3.14;
        a=v/aa;
        printf("ALTURA = %.2lf\n"
               "AREA = %.2lf\n",a,aa);
    }
    return 0;
}