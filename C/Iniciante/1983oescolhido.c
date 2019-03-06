#include <stdio.h>
#include <stdlib.h>
int main(){
    double *nota, mn = 0;
    int n,i,*mat, mp = 0;
    scanf("%d",&n);
    mat=(int *)malloc(n* sizeof(int));
    nota=(double *)malloc(n* sizeof(double));
    for(i=0;i<n;i++){
        scanf("%d%lf", &mat[i], &nota[i]);
        if(i==0){
            mp=i;
            mn=nota[i];
        }
        if(mn<=nota[i]){
            mp=i;
            mn=nota[i];
        }
    }
    if(mn>=8){
        printf("%d\n",mat[mp]);
    }else{
        printf("Minimum note not reached\n");
    }
    return 0;
}