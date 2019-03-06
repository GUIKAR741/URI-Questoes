#include <stdio.h>
#include <math.h>
int main() {
    int x,y,i=1,j;
    scanf("%d%d",&x,&y);
    while(i<y){
        for(j=0;j<x-1;j++){
            printf("%d ",i);
            i++;
        }
        printf("%d\n",i);
        i++;
    }
    return 0;
}