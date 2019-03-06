#include <stdio.h>
#include <string.h>
int main(){
    int c,lenght;
    char pala[10100];
    scanf("%d",&c);
    while (c--){
        scanf("%s",pala);
        lenght=strlen(pala);
        printf("%.2lf\n",lenght*.01);
    }
    return 0;
}