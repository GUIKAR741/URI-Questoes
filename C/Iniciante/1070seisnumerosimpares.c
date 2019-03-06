#include <stdio.h>
int main() {
    int A,i,C;
    scanf("%d",&A);
    if(A%2==0){
        A+=1;
        C=5;
        printf("%d\n",A);
    }else{
        C=6;
    }
    for(i=1;i<=C;i++){
        A+=2;
        printf("%d\n",A);
    }
    return 0;
}