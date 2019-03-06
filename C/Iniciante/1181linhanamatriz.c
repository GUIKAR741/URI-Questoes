#include <stdio.h>
#define QTD 12
int main() {
    int i,j,l;
    float matriz[QTD][QTD],conta=0;
    char t;
    scanf("%d %c",&l,&t);
    for(i=0;i<QTD;i++){
        for(j=0;j<QTD;j++){
            scanf("%f",&matriz[i][j]);
        }
    }
    for(i=0;i<QTD;i++){
        conta+=matriz[l][i];
    }
    if(t=='S'){
        printf("%.1f\n",conta);
    }
    if(t=='M'){
        printf("%.1f\n",conta/QTD);
    }
    return 0;
}