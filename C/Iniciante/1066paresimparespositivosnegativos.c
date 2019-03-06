#include <stdio.h>
int main() {
    int A,i,P=0,N=0,p=0,n=0;
    for(i=1;i<=5;i++){
        scanf("%d",&A);
        if(A%2==0){
            P++;
        }else{
            N++;
        }
        if(A>0)p++;
        if(A<0)n++;
    }
    printf("%d valor(es) par(es)\n",P);
    printf("%d valor(es) impar(es)\n",N);
    printf("%d valor(es) positivo(s)\n",p);
    printf("%d valor(es) negativo(s)\n",n);
    return 0;
}