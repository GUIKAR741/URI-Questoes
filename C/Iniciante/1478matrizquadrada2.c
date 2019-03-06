#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,j,k,p,n;
    while(1){
        scanf("%d",&n);
        if(n==0)break;
        int **mat;
        mat=(int **) malloc(n*sizeof(int *));
        for(i=0;i<n;i++){
            mat[i]=(int*) malloc(n*sizeof(int));
        }
        for(i=0,k=1;i<n;i++,k--){
            for(j=i;j<n;j++){
                mat[i][j]=j+k;
                mat[j][i]=mat[i][j];
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<n-1;j++){
                printf("%3d ",mat[i][j]);
            }
            printf("%3d\n",mat[i][j]);
        }
        printf("\n");
        for(i=0;i<n;i++){
            free(mat[i]);
        }
        free(mat);
    };
    return 0;
}