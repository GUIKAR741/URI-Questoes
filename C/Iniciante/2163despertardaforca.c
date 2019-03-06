#include <stdio.h>
#include <stdlib.h>
int sabre(int **c,int a,int b){
    int i,j,cont=0;
    for(i=a-1;i<=a+1;i++)
        for(j=b-1;j<=b+1;j++){
            if(c[i][j]==7){
                cont++;
            }
        }
    return cont;
}
int main(){
    int m,n,**campo,i,j,k=0;
    scanf("%d %d",&m,&n);
    campo=(int **) malloc(m* sizeof(int *));
    for(i=0;i<n;i++)campo[i]=(int *)malloc(n* sizeof(int));
    for(i=0;i<m;i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &campo[i][j]);
        }
    }
    for(i=0;i<m;i++) {
        for (j = 0; j < n; j++) {
            if (campo[i][j] == 42) {
                if (sabre(campo, i, j) == 8) {
                    printf("%d %d\n",i+1,j+1);
                    k++;
                }
            }
        }
    }
    if(k!=1)printf("%d %d\n",0,0);
    return 0;
}