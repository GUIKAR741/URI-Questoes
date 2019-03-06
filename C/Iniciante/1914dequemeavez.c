#include <stdio.h>
#include <string.h>
int main(){
    int a,i=0;
    scanf("%d",&a);
    while (i++<a){
        int r1,r2,res;
        char n1[20],n2[20],op1[10],op2[10];
        scanf(" %s %s %s %s",n1,op1,n2,op2);
        scanf(" %d %d",&r1,&r2);
        res=(r1+r2)%2;
        if(res==0){
            if(strcmp(op1,"PAR")==0){
                printf("%s\n",n1);
            }else{
                printf("%s\n",n2);
            }
        }else{
            if(strcmp(op1,"PAR")==0){
                printf("%s\n",n2);
            } else{
                printf("%s\n",n1);
            }
        }
    }
    return 0;
}