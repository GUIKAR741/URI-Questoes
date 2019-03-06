#include <stdio.h>
int main() {
    int n,i,x,y;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        scanf("%i%i",&x,&y);
        if(y!=0){
            printf("%.1lf\n", (double) x / y);
        }else{
            printf("divisao impossivel\n");
        }
    }
    return 0;
}