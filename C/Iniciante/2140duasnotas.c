#include <stdio.h>
int cedulas(int n){
    int c100,c50,c20,c10,c5,c2,c1;
    c100=n/100;
    n-=c100*100;
    c50=n/50;
    n-=c50*50;
    c20=n/20;
    n-=c20*20;
    c10=n/10;
    n-=c10*10;
    c5=n/5;
    n-=c5*5;
    c2=n/2;
    n-=c2*2;
    c1=n/1;
    return c100+c50+c20+c10+c5+c2+c1;
}
int main(){
    int m,n,troco;
    while (1){
        scanf("%d %d",&m,&n);
        if(m==0 && n==0)break;
        troco=cedulas(n-m);
        if(troco==2) printf("possible\n");
        else printf("impossible\n");
    }
    return 0;
}