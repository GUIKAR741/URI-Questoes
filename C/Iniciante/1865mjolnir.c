#include <stdio.h>
#include <string.h>
int main(){
    int a,i=0,forca;
    char nome[30];
    scanf("%d",&a);
    while (i++<a){
        scanf("%s %d",nome,&forca);
        if(strcmp(nome,"Thor")==0)printf("Y\n");
        else printf("N\n");
    }
    return 0;
}