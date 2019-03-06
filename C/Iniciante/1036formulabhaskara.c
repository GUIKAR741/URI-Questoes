#include <stdio.h>
#include <math.h>
int main() {
    double A,B,C,delta,r1,r2;
    scanf("%lf%lf%lf",&A,&B,&C);
    delta=pow(B,2)-4.0*A*C;
    if(A!=0){
        if(delta>=0){
            r1=(-B+sqrt(delta))/(2.0*A);
            r2=(-B-sqrt(delta))/(2.0*A);
            printf("R1 = %.5lf\nR2 = %.5lf\n",r1,r2);
        }else{
            printf("Impossivel calcular\n");
        }
    }else{
        printf("Impossivel calcular\n");
    }
    return 0;
}