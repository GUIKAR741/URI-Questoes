#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int verTipo(char re[10]){
    if(strcmp(re,"pedra")==0)return 1;
    else if(strcmp(re,"papel")==0)return 2;
    else if(strcmp(re,"ataque")==0)return 3;
}
int ganhou(int r1,int r2){
    if(r1==3 && r2==1){return 1;}
    if(r1==1 && r2==3){return 2;}
    if(r1==1 && r2==2){return 1;}
    if(r1==2 && r2==1){return 2;}
    if(r1==3 && r2==2){return 1;}
    if(r1==2 && r2==3){return 2;}
    if(r1==2 && r2==2){return 5;}
    if(r1==1 && r2==1){return 3;}
    if(r1==3 && r2==3){return 4;}
    return 2;
}
int jogar(char re1[10],char re2[10]){
    int r1,r2;
    r1=verTipo(re1);
    r2=verTipo(re2);
    return ganhou(r1,r2);
}
int main(){
    int n,i=0,ret;
    scanf("%d",&n);
    while(i++<n){
        char res1[10],res2[10];
        scanf("%s %s",res1,res2);
        ret=jogar(res1,res2);
        if(ret==1)printf("Jogador 1 venceu\n");
        if(ret==2)printf("Jogador 2 venceu\n",i);
        if(ret==3)printf("Sem ganhador\n",i);
        if(ret==4)printf("Aniquilacao mutua\n",i);
        if(ret==5)printf("Ambos venceram\n",i);
    };
    return 0;
}