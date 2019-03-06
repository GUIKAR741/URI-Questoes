#include <stdio.h>
int main() {
    int i,P=0;
    double n;
    for(i=1;i<=6;i++){
        scanf("%lf",&n);
        if(n>0){
            P++;
        }
    }
    printf("%i valores positivos\n",P);
    return 0;
}