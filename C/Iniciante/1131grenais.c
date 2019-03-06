#include <stdio.h>
int main() {
    int i=0,tipo,n,in,gr,vin=0,vgr=0,em=0;
    do {
        scanf("%d%d",&in,&gr);
        i++;
        if(in==gr){
            em++;
        } else if(in>gr){
            vin++;
        } else if(in<gr){
            vgr++;
        }
        while (1) {
            printf("Novo grenal (1-sim 2-nao)\n");
            scanf("%d", &tipo);
            if(tipo==1 || tipo==2)break;
        }
    }while(tipo!=2);
    printf("%d grenais\n"
           "Inter:%d\n"
           "Gremio:%d\n"
           "Empates:%d\n",i,vin,vgr,em);
    if(vin>vgr){
        printf("Inter venceu mais\n");
    } else if(vin<vgr){
        printf("Gremio venceu mais\n");
    }else if(vin==vgr){
        printf("Nao houve vencedor\n");
    }
    return 0;
}