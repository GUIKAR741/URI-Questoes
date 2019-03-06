#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int verTipo(char re[10]){
    if(strcmp(re,"pedra")==0)return 1;
    else if(strcmp(re,"papel")==0)return 2;
    else if(strcmp(re,"tesoura")==0)return 3;
    else if(strcmp(re,"lagarto")==0)return 4;
    else if(strcmp(re,"Spock")==0)return 5;
}
int ganhou(int r1,int r2){
    if(r1==3 && r2==2){return 1;}
    if(r1==2 && r2==1){return 1;}
    if(r1==1 && r2==4){return 1;}
    if(r1==4 && r2==5){return 1;}
    if(r1==5 && r2==3){return 1;}
    if(r1==3 && r2==4){return 1;}
    if(r1==4 && r2==2){return 1;}
    if(r1==2 && r2==5){return 1;}
    if(r1==5 && r2==1){return 1;}
    if(r1==1 && r2==3){return 1;}
    return 2;
}
int bazinga(char re1[10],char re2[10]){
    int r1,r2;
    r1=verTipo(re1);
    r2=verTipo(re2);
    if(r1==r2)
        return 3;
    return ganhou(r1,r2);
}
int main(){
    int n,i=0,ret;
    scanf("%d",&n);
    while(i++<n){
        char res1[10],res2[10];
        scanf("%s %s",res1,res2);
        ret=bazinga(res1,res2);
        if(ret==1)printf("Caso #%d: Bazinga!\n",i);
        if(ret==2)printf("Caso #%d: Raj trapaceou!\n",i);
        if(ret==3)printf("Caso #%d: De novo!\n",i);
    };
    return 0;
}