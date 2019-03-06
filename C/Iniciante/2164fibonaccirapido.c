#include <stdio.h>
#include <math.h>
int main(){
    int n;
    double p1,p2,fib;
    scanf("%d",&n);
    p1=pow(((1+sqrt(5.0))/2),n);
    p2=pow(((1-sqrt(5.0))/2),n);
    fib=(p1-p2)/sqrt(5.0);
    printf("%.1lf",fib);
    return 0;
}