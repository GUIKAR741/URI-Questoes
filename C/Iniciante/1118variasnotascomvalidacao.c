#include <stdio.h>
int main() {
    int i=0,tipo;
    double n,soma=0;
    do {
        do {
            scanf("%lf", &n);
            if (n >= 0 && n <= 10) {
                soma += n;
                i++;
            } else {
                printf("nota invalida\n");
            }
        } while (i < 2);
        printf("media = %.2lf\n",soma/2);
        i=0;
        soma=0;
        while (1) {
            printf("novo calculo (1-sim 2-nao)\n");
            scanf("%d", &tipo);
            if(tipo==1 || tipo==2)break;
        }
    }while(tipo!=2);
    return 0;
}