#include <stdio.h>
int main(){
    int m,d,meses[]={31,29,31,30,31,30,31,31,30,31,30,31},i,dia;
    while (scanf("%d %d",&m,&d)!=EOF){
        dia=0;
        for(i=0;i<m-1;i++){
            dia+=meses[i];
        }
        dia+=d;
        if(dia==360)printf("E natal!\n");
        else if(dia==359)printf("E vespera de natal!\n");
        else if(dia>360)printf("Ja passou!\n");
        else{
            printf("Faltam %d dias para o natal!\n",360-dia);
        }
    }
    return 0;
}