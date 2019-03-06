#include <stdio.h>
int main() {
    int n,x,y,i,j,soma;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        soma=0;
        scanf("%d%d",&x,&y);
        if((x%2)==0) {
            x += 1;
        }
        for(j=1;j<=y;j++){
            soma+=x;
            x+=2;
        }
        printf("%d\n",soma);
    }
    return 0;
}