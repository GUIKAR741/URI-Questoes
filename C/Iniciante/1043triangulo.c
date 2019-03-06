#include <stdio.h>
#include <math.h>
int main() {
    double a,b,c,calc,ab,ac,bc,aab,aac,abc;
    scanf("%lf%lf%lf",&a,&b,&c);
    ab=a+b;
    ac=a+c;
    bc=b+c;
    aab=fabs(a-b);
    aac=fabs(a-c);
    abc=fabs(b-c);
    if((abc<a && a<bc)&&(aac<b && b<ac)&&(aab<c && a<ab)){
        calc=a+b+c;
        printf("Perimetro = %.1lf\n",calc);
    }else{
        calc=((a+b)/2)*c;
        printf("Area = %.1lf\n",calc);
    }
    return 0;
}