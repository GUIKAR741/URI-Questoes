#include <stdio.h>
int main() {
    int m,p,i,v;
    scanf("%d",&v);
    int x[v];
    scanf("%d",&x[0]);
    m=x[0];
    p=0;
    for(i=1;i<v;i++){
        scanf("%d",&x[i]);
        if(x[i]<m){
            m=x[i];
            p=i;
        }
    }
    printf("Menor valor: %d\n"
           "Posicao: %d\n",m,p);
    return 0;
}