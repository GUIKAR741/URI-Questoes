#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int dg(int x){
    int a=x,b=0;
    while(a)
    {
        a/=10;
        b++;
    }
    return b;
}
int main()
{
    int i,j,k,p=0,l=0,n;
    while(1){
        scanf("%d",&n);
        if(n==0)break;
        int **mat;
        mat=(int **) malloc(n*sizeof(int *));
        for(i=0;i<n;i++){
            mat[i]=(int*) malloc(n*sizeof(int));
        }
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                mat[i][j]= (int) pow(2, i+j);
            }
        }
        p=dg(mat[n-1][n-1]);
        for(i=0;i<n;i++){

            for(j=0;j<n;j++){
                l=dg(mat[i][j]);
                for(k=1;k<=(p-l);k++)printf(" ");
                j==0?printf("%d",mat[i][j]):printf(" %d",mat[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        for(i=0;i<n;i++){
            free(mat[i]);
        }
        free(mat);
    };
    return 0;
}