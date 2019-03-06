#include <stdio.h>
int main() {
    int m,n,soma,mm,mn,i;
    scanf("%d%d",&m,&n);
    while(1){
        if(m<=0 || n<=0)break;
        if(m<n){
            mm=m;
            mn=n;
        }else{
            mm=n;
            mn=m;
        }
        soma=0;
        for(i=mm;i<=mn;i++){
            printf("%d ",i);
            soma+=i;
        }
        printf("Sum=%d\n",soma);
        scanf("%d%d",&m,&n);
    }
    return 0;
}