#include <stdio.h>
#include <stdlib.h>
int main(){
    int n,i;
    double qtd,total=0,val[]={0,1.5,2.5,3.5,4.5,5.5};
    scanf("%d",&n);
    while (n--){
        scanf("%d%lf",&i,&qtd);
        total+=val[(i-1000)]*qtd;
    }
    printf("%.2lf\n",total);
    return 0;
}