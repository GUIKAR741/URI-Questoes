#include <stdio.h>
int main() {
    int i,P=0,n;
    for(i=1;i<=5;i++){
        scanf("%i",&n);
        if(n%2==0){
            P++;
        }
    }
    printf("%i valores pares\n",P);
    return 0;
}