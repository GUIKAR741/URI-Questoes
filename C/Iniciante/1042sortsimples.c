#include <stdio.h>
#include <math.h>
int main() {
    int a,b,c,ao,bo,co;
    scanf("%i%i%i",&a,&b,&c);
    ao=a;
    bo=b;
    co=c;
    if (a > c) {
        int tmp = c;
        c = a;
        a = tmp;
    }
    if (a > b) {
        int tmp = b;
        b = a;
        a = tmp;
    }
    if (b > c) {
        int tmp = c;
        c = b;
        b = tmp;
    }
    printf("%i\n%i\n%i\n\n%i\n%i\n%i\n",a,b,c,ao,bo,co);
    return 0;
}