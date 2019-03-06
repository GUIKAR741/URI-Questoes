#include <stdio.h>
int main() {
    int n,ano,mes,dia;
    scanf("%i",&n);
    ano=n/365;
    n-=ano*365;
    mes=n/30;
    n-=mes*30;
    dia=n;
    printf("%i ano(s)\n"
           "%i mes(es)\n"
           "%i dia(s)\n",ano,mes,dia);
    return 0;
}