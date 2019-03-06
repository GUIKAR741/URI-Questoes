#include <stdio.h>
int main() {
    int x,y,mx,my,i;
    scanf("%d%d",&x,&y);
    if(x<y){
        mx=x;
        my=y;
    }else{
        mx=y;
        my=x;
    }
    for (i = mx+1; i < my; i++) {
        if((i%5)==2 || (i%5)==3){
            printf("%d\n",i);
        }
    }
    return 0;
}