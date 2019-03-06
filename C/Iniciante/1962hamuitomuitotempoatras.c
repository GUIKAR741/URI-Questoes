#include <stdio.h>
int main(){
    int n,t,i=0;
    scanf("%d",&n);
    while (i++<n){
        scanf("%d",&t);
        if(t<2015){
            printf("%d D.C.\n",(2015-t));
        }else{
            printf("%d A.C.\n",(t-2014));
        }
    }
}