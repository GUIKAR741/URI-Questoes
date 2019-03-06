#include <stdio.h>
int main() {
    int n,i,m=0,p=0,pp;
    for(i=1;i<=100;i++){
        scanf("%d",&n);
        p++;
        if(n>m){
            m=n;
            pp=p;
        }
    }
    printf("%d\n%d\n",m,pp);
    return 0;
}