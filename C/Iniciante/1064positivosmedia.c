#include <stdio.h>
int main() {
    int i,P=0;
    double n,soma=0;
    for(i=1;i<=6;i++){
        scanf("%lf",&n);
        if(n>0){
            P++;
            soma+=n;
        }
    }
    printf("%i valores positivos\n",P);
    printf("%.1lf\n",(soma/P));
    return 0;
}