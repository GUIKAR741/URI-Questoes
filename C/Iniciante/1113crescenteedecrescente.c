#include <stdio.h>
int main() {
    int m,n;
    scanf("%d%d",&m,&n);
    while(m!=n){
        if(m>n){
            printf("Decrescente\n");
        }else{
            printf("Crescente\n");
        }
        scanf("%d%d",&m,&n);
    }
    return 0;
}