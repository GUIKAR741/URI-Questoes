#include <stdio.h>
int main(){
    long double x;
    char s[120];
    scanf("%LE",&x);
    sprintf(s,"%LE",x);
    if(s[0]!='-')printf("+");
    printf("%.4LE\n",x);
    return 0;
}