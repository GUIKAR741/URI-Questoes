#include <stdio.h>
int main() {
    int A,N,i,soma=0;
    scanf("%i %i",&A,&N);
    while(N<=0){
        scanf("%i",&N);
    }
    for(i=0;i<(N);i++){
        soma+=A+i;
    }
    printf("%i\n",soma);
    return 0;
}