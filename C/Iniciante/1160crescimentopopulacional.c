#include <stdio.h>
int main() {
    int n,pa,pb,i,j;
    double g1,g2;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d%d%lf%lf",&pa,&pb,&g1,&g2);
        j=0;
        while(pa<=pb){
            pa= (int) (pa + (pa * (g1 / 100)));
            pb= (int) (pb + (pb * (g2 / 100)));
            j++;
            if(j>100){
                break;
            }
        }
        if(j>100){
            printf("Mais de 1 seculo.\n");
        }else{
            printf("%i anos.\n",j);
        }
    }
    return 0;
}