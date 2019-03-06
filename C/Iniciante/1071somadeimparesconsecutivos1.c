#include <stdio.h>
int main() {
    int x,y,ma,me,soma=0,i;
    scanf("%d %d",&x,&y);
    if(x>y){
        ma=x;
        me=y;
    }else{
        ma=y;
        me=x;
    }
    for(i=me+1;i<ma;i++){
        if((i%2)!=0){
            soma+=i;
        }
    }
    printf("%d\n",soma);
    return 0;
}