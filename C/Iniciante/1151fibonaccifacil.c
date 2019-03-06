#include <stdio.h>
int main() {
    int A,B,aux,N,i;
    scanf("%i",&N);
    A=0;
    B=1;
    printf("%i %i",A,B);
    for(i=2;i<N;i++){
        aux=B;
        B=A+aux;
        A=aux;
        printf(" %i",B);
    }
    printf("\n");
    return 0;
}