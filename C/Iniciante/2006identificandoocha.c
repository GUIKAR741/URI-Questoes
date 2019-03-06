#include <stdio.h>
#include <stdlib.h>
int main(){
    int n,i,v[5],c=0;
    scanf("%d",&n);
    for(i=0;i<5;i++){
        scanf("%d",&v[i]);
        if(v[i]==n)c++;
    }
    printf("%d\n",c);
    return 0;
}