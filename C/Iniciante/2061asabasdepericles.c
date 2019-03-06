#include <stdio.h>
#include <string.h>
int main(){
    int n,m;
    char acao[10];
    scanf("%d %d",&n,&m);
    while (m--){
        scanf(" %s",acao);
        if(strcmp(acao,"fechou")==0){
            n++;
        }else if(strcmp(acao,"clicou")==0){
            n--;
        }
    }
    printf("%d\n",n);
    return 0;
}