#include <stdio.h>
#include <stdlib.h>
int main(){
    int l;
    while(scanf("%d",&l)!=EOF){
        int *v,i,max;
        v=(int *) malloc(l* sizeof(int));
        scanf("%d",&v[0]);
        max=v[0];
        for(i=1;i<l;i++){
            scanf("%d",&v[i]);
            if(v[i]>max)max=v[i];
        }
        if(max<10)printf("1\n");
        else if(max<20)printf("2\n");
        else printf("3\n");
        free(v);
    };
    return 0;
}