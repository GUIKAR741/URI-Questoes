#include <stdio.h>
int main() {
    int n,c100,c50,c20,c10,c5,c2,c1;
    scanf("%i",&n);
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
    n=c100*100+c50*50+c20*20+c10*10+c5*5+c2*2+c1*1;
    printf("%i\n"
           "%i nota(s) de R$ 100,00\n"
           "%i nota(s) de R$ 50,00\n"
           "%i nota(s) de R$ 20,00\n"
           "%i nota(s) de R$ 10,00\n"
           "%i nota(s) de R$ 5,00\n"
           "%i nota(s) de R$ 2,00\n"
           "%i nota(s) de R$ 1,00\n", n,c100,c50,c20,c10,c5,c2,c1);
    return 0;
}