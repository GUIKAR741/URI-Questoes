#include <stdio.h>
#include <stdlib.h>
int main(){
    int p,n,i,*t,r=0,d;
    scanf("%d%d",&p,&n);
    t=(int *)malloc(n* sizeof(int));
    for(i=0;i<n;i++){
        scanf("%d",&t[i]);
    }
    for(i=1;i<n;i++){
        d=(t[i]-t[i-1]);
        if(d<0)d=d*-1;
        if((d>p)){
            printf("GAME OVER\n");
            r--;
            break;
        }
    }
    if(r==0)printf("YOU WIN\n");
    return 0;
}