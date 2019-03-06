#include <stdio.h>
#include <math.h>
int main(){
    int a,i=0;
    scanf("%d",&a);
    while (i++<a){
        int termo,j,soma=0;
        scanf("%d",&termo);
        for(j=0;j<termo;j++){
            soma+=(1*pow(-1,j));
        }
        printf("%d\n",soma);
    }
    return 0;
}