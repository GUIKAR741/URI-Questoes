#include <stdio.h>
int main() {
    int N,i,fat=1;
    scanf("%i",&N);
    for(i=N;i>0;i--){
        fat*=i;
    }
    printf("%i\n",fat);
    return 0;
}