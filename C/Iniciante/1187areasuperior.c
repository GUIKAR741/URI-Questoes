#include <stdio.h>
#define QTD 12
int main() {
    int i,j,c=0;
    double matriz[QTD][QTD],conta=0;
    char t;
    scanf("%c",&t);
    for(i=0;i<QTD;i++){
        for(j=0;j<QTD;j++){
            scanf("%lf",&matriz[i][j]);
        }
    }
    for(i=0;i<QTD;i++){
        for(j=0;j<QTD;j++){
            if(i<j &&(i+j)<QTD-1) {
                conta += matriz[i][j];
                c++;
            }
        }
    }
    if(t=='S'){
        printf("%.1lf\n",conta);
    }
    if(t=='M'){
        printf("%.1lf\n",conta/c);
    }
    return 0;
}