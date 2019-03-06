#include <stdio.h>
int main() {
    int i=1,j=7,k=1,n=7;
    while (i<10){
        printf("I=%d J=%d\n",i,j);
        j-=1;
        k++;
        if(k==4){
            k=1;
            i+=2;
            n+=2;
            j=n;
        }
    }
    return 0;
}