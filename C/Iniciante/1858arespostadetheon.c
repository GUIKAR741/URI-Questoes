#include <stdio.h>
#include <stdlib.h>
int main(){
    int n,i=0,*t, pessoa = 0, num = 0;
    scanf("%d",&n);
    t=(int *)malloc(n* sizeof(int));
    for(i=0;i<n;i++){
        scanf("%d",&t[i]);
        if(i==0){
            num=t[i];
            pessoa=i+1;
        }
        if(num>t[i]){
            num=t[i];
            pessoa=i+1;
        }
    }
    printf("%d\n",pessoa);
    free(t);
    return 0;
}