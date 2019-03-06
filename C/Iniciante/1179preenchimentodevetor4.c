#include <stdio.h>
//1 3 4 -4 2 3 8 2 5 -7 54 76 789 23 98
int main() {
    int par[5],impar[5],i,v,j,p=0,ii=0;
    for(i=1;i<=15;i++){
        scanf("%d",&v);
        if((v%2)==0){
            par[p++]=v;
        }else{
            impar[ii++]=v;
        }
        if(p==5){
            for(j=0;j<p;j++){
                printf("par[%d] = %d\n",j,par[j]);
            }
            p=0;
        }
        if(ii==5){
            for(j=0;j<ii;j++){
                printf("impar[%d] = %d\n",j,impar[j]);
            }
            ii=0;
        }
    }
    for(i=0;i<ii;i++){
        printf("impar[%d] = %d\n",i,impar[i]);
    }
    for(i=0;i<p;i++){
        printf("par[%d] = %d\n",i,par[i]);
    }
    return 0;
}