#include <stdio.h>
int main() {
    int n,i,j,x,y,soma,mx,my;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        soma=0;
        scanf("%d %d",&x,&y);
        if(x<y){
            mx=x;
            my=y;
        }else{
            mx=y;
            my=x;
        }
        for (j = mx+1; j < my; j++) {
            if((j%2)!=0){
                soma+=j;
            }
        }
        printf("%d\n",soma);
    }
    return 0;
}