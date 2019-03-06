#include <stdio.h>
#include <stdlib.h>
int main(){
    int n,*num,i,mult[4];
    scanf("%d",&n);
    num=(int *)malloc(n* sizeof(int));
    for(i=0;i<4;i++)mult[i]=0;
    for(i=0;i<n;i++){
        scanf("%d",&num[i]);
        if((num[i]%2)==0)mult[0]++;
        if((num[i]%3)==0)mult[1]++;
        if((num[i]%4)==0)mult[2]++;
        if((num[i]%5)==0)mult[3]++;
    }
    printf("%d Multiplo(s) de 2\n"
           "%d Multiplo(s) de 3\n"
           "%d Multiplo(s) de 4\n"
           "%d Multiplo(s) de 5\n",mult[0],mult[1],mult[2],mult[3]);
    return 0;
}