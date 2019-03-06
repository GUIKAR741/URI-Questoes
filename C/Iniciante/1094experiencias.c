#include <stdio.h>
int main() {
    int n,i,a,c=0,r=0,s=0,t=0;
    char tipo;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        scanf("%d %c",&a,&tipo);
        if(tipo=='C'){
            c+=a;
        }else if(tipo=='R'){
            r+=a;
        }else if(tipo=='S'){
            s+=a;
        }
        t+=a;
    }
    printf("Total: %d cobaias\n"
           "Total de coelhos: %d\n"
           "Total de ratos: %d\n"
           "Total de sapos: %d\n"
           "Percentual de coelhos: %.2lf %%\n"
           "Percentual de ratos: %.2lf %%\n"
           "Percentual de sapos: %.2lf %%\n", (c+r+s), c, r, s, (100.0 * c / t),(100.0 * r / t),(100.0 * s / t));
    return 0;
}