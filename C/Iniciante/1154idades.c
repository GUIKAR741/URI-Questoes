#include <stdio.h>
int main() {
    int i=0;
    float N,acm=0;
    do {
        scanf("%f", &N);
        if(N>0) {
            acm += N;
            i++;
        }
    }while (N>0);
    printf("%.2f\n",acm/i);
    return 0;
}