#include <stdio.h>
int main() {
    double S=1,i,a=2;
    for(i=3;i<=39;i+=2){
        S+=i/a;
        a*=2;
    }
    printf("%.2lf\n",S);
    return 0;
}