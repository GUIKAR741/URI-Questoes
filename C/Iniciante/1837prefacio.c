#include <stdio.h>
int main(){
    int a,b,r, f = 0,i;
    scanf("%d%d",&a,&b);
    if(a<0){
        i=b;
        if(b<0)i=b*-1;
        for(r=0;r<i;r++) {
            f=a-r;
            if(f%b==0)break;
        }
        printf("%d %d\n", f/b,r);
    }else {
        printf("%d %d\n", a/b, a%b);
    }
    return 0;
}