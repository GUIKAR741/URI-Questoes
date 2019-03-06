#include <stdio.h>
int main(){
    int n,i=0,j,k, qtd;
    while (scanf("%d",&n)!=EOF){
        qtd=1;
        qtd += ((n*(n + 1)) / 2);
        i++;
        if(n==0)printf("Caso %d: %d numero\n",i,qtd);
        else printf("Caso %d: %d numeros\n", i, qtd);
        printf("0");
        for(j=1;j<=n;j++){
            for(k=1;k<=j;k++)printf(" %d",j);
        }
        printf("\n\n");
    }
    return 0;
}