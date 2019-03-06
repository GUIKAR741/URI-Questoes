#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,j,k,p,n;
    while(scanf("%d",&n)!=EOF){
        int **mat;
        mat=(int **) malloc(n*sizeof(int *));
        for(i=0;i<n;i++){
            mat[i]=(int*) malloc(n*sizeof(int));
        }
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(j==i)mat[i][j]=1;
                if(j==n-1-i){mat[i][j]=2;}
                else if(j!=i && j!=(n-1-i)){mat[i][j]=3;}
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                printf("%d",mat[i][j]);
            }
            printf("\n");
        }
//        printf("\n");
        for(i=0;i<n;i++){
            free(mat[i]);
        }
        free(mat);

    };
    return 0;
}
