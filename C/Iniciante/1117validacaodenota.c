#include <stdio.h>
int main() {
    int i=0;
    double n,soma=0;
    do{
        scanf("%lf",&n);
        if(n>=0 && n<=10){
            soma+=n;
            i++;
        }else{
            printf("nota invalida\n");
        }
    }while (i<2);
    printf("media = %.2lf\n",soma/2);
    return 0;
}