#include <stdio.h>
#include <stdlib.h>
int main(){
    long long int n,*c,*s,i,somares=0,soma=0;
    scanf("%lli",&n);
    c=(long long int *)malloc((size_t) (n * sizeof(long long int)));
    s=(long long int *)malloc((size_t) (n * sizeof(long long int)));
    for(i=0;i<n;i++){
        scanf("%lli",&c[i]);
        s[i]=0;
    }
    i=0;
    while (1) {
        if(i==0 && c[i]%2==0)
        {
            s[i]=1;
            if(c[i]>0)
                c[i]--;
            break;
        }
        else if(i==n-1 && c[i]%2==1)
        {
            s[i]=1;
            if(c[i]>0)
                c[i]--;
            break;
        }
        else if(c[i]%2==1)
        {
            c[i]--;
            s[i]=1;
            i++;
        }
        else if(c[i]%2==0)
        {
            s[i]=1;
            if(c[i]>0)
                c[i]--;
            i--;
        }
    }
    for(i=0;i<n;i++){
        somares+=c[i];
        soma+=s[i];
    }
    printf("%lli %lli\n",soma,somares);
    return 0;
}