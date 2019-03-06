#include <stdio.h>
int main() {
    int x,j,soma,a;
    do{
        scanf("%d",&x);
        a=x;
        soma=0;
        if(a!=0) {
            if ((a % 2) != 0) {
                a += 1;
            }
            for (j = 1; j <= 5; j++) {
                soma += a;
                a += 2;
            }
            printf("%d\n", soma);
        }
    }while (x!=0);
    return 0;
}