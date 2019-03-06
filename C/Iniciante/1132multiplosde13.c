#include <stdio.h>
#include <math.h>
int main() {
    int x,y,i,my,mx,soma=0;
    scanf("%d %d",&x,&y);
    if(x<y){
        mx=x;
        my=y;
    }else{
        mx=y;
        my=x;
    }
    for(i=mx;i<=my;i++){
        if((i%13)!=0){
            soma+=i;
        }
    }
    printf("%d\n",soma);
    return 0;
}