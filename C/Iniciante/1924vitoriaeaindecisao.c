#include <stdio.h>
int main(){
    int a,i=0;
    char curso[30];
    scanf("%d",&a);
    while (i++<a){
        scanf(" %[^\n]s",curso);
    }
    printf("Ciencia da Computacao\n");
    return 0;
}