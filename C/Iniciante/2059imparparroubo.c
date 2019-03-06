#include <stdio.h>
int main(){
    int p,j1,j2,r,a,soma;
    scanf("%d%d%d%d%d",&p,&j1,&j2,&r,&a);
    soma=(j1+j2)%2;
    if(r==0 && a==0){
        if((soma==0 && p==1)||(soma!=0 && p!=1)){
            printf("Jogador 1 ganha!\n");
        }else {
            printf("Jogador 2 ganha!\n");
        }
    }else if((r==1 && a==0)||(r==0 && a==1)){
        printf("Jogador 1 ganha!\n");
    }else{
        printf("Jogador 2 ganha!\n");
    }
    return 0;
}