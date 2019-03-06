#include <stdio.h>
int main() {
    int x,y;
    scanf("%d%d", &x, &y);
    while (1){
        if(x==0 || y==0)break;
        if (x > 0 && y > 0) {
            //q1
            printf("primeiro\n");
        } else if (x < 0 && y > 0) {
            //q2
            printf("segundo\n");
        } else if (x < 0 && y < 0) {
            //q3
            printf("terceiro\n");
        } else if (x > 0 && y < 0) {
            //q4
            printf("quarto\n");
        }
        scanf("%d%d", &x, &y);
    }
    return 0;
}