#include <stdio.h>
#include <stdlib.h>
int main(){
    int n;
    while(scanf("%d",&n)!=EOF){
        int **m,i,j;
        m=(int **)malloc(n* sizeof(int *));
        for(i=0;i<n;i++)m[i]=(int *)malloc(n*sizeof(int));
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                m[i][j]=0;
        for(i=0;i<n;i++){
            m[i][i]=2;
            m[i][n-1-i]=3;
        }
        for(i=(n/3);i<(n-(n/3));i++)
            for(j=(n/3);j<(n-(n/3));j++)
                m[i][j]=1;
        for(i=0;i<=(n/2);i++)if(i==(n/2))m[i][i]=4;
        for(i=0;i<n;i++) {
            for (j = 0; j < n; j++){
                printf("%d",m[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    };
    return 0;
}