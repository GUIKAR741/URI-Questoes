#include <stdio.h>
int main() {
    unsigned long long int p1,p2,j,p;
    int t,n,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d",&n);
        p1=0;
        p2=1;
        n++;
        for(j=0;j<n;j++){
            if (j <= 1) p = j;
            else
            {
                p = p1+p2;
                p1= p2;
                p2= p;
            }
        }
        printf("Fib(%d) = %llu\n",n-1,p);
    }
    return 0;
}