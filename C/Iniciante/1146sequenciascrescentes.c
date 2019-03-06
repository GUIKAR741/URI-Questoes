#include <stdio.h>
int main() {
    int x,i;
    do{
        scanf("%i",&x);
        for(i=1;i<x;i++){
            printf("%i ",i);
        }
        if(x!=0) {
            printf("%i\n", i);
        }
    }while(x!=0);
    return 0;
}