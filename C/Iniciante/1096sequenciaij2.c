#include <stdio.h>
int main() {
    int i=1,j=7,k=1;
    while (i<10){
        printf("I=%d J=%d\n",i,j);
        j-=1;
        k++;
        if(k==4){
            k=1;
            i+=2;
            j=7;
        }
    }
    return 0;
}