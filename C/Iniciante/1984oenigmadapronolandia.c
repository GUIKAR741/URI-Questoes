#include <stdio.h>
#include <stdlib.h>
int main(){
    unsigned long long int n,i,r;
    scanf("%llu",&n);
    while (n){
        r=n%10;
        printf("%llu",r);
        n/=10;
    }
    printf("\n");
    return 0;
}