#include <stdio.h>
int main(){
    int a,i=0;
    char hex[]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'},dec[100];
    scanf("%d",&a);
    while (a>=16){
        dec[i++]=hex[a%16];
        a/=16;
    }
    dec[i]=hex[a];
    while (i>=0){
        printf("%c",dec[i--]);
    }
    printf("\n");
    return 0;
}