#include <stdio.h>
int main(){
    int a,i;
    char frase[]= "LIFE IS NOT A PROBLEM TO BE SOLVED";
    scanf("%d",&a);
    for(i=0;i<a;i++){
        printf("%c",frase[i]);
    }
    printf("\n");
    return 0;
}