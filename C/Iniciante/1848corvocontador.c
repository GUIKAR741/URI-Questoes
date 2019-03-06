#include <stdio.h>
#include <string.h>
int main(){
    int a=0,i=0,caw=0,conta[]={4,2,1};
    char corvo[10];
    while (caw<3){
        scanf(" %[^\n]s", corvo);
        if(strcmp(corvo,"caw caw")==0){
            printf("%d\n",a);
            a=0;
            caw++;
        }else{
            i=0;
            while (corvo[i]!='\0'){
                if(corvo[i]=='*'){
                    a+=conta[i];
                }
                i++;
            }
        }
    }
    return 0;
}