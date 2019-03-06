#include <stdio.h>
int main() {
    int A,Z,i=1,soma;
    scanf("%i",&A);
    soma=A;
    do{
        scanf("%i",&Z);
    }while(Z<=A);
    while (soma<Z){
        soma+=A+i;
        i++;
    }
    printf("%i\n",(i));
    return 0;
}