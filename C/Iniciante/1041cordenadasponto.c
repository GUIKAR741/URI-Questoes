#include <stdio.h>
int main() {
    double x,y;
    scanf("%lf%lf",&x,&y);
    if(x==0 && y==0){
        //origem
        printf("Origem\n");
    }else if(x==0 && y!=0){
        //eixo x
        printf("Eixo Y\n");
    }else if(x!=0 && y==0) {
        //eixo y
        printf("Eixo X\n");
    }else if(x>0 && y>0){
        //q1
        printf("Q1\n");
    }else if(x<0 && y>0){
        //q2
        printf("Q2\n");
    }else if(x<0 && y<0){
        //q3
        printf("Q3\n");
    }else if(x>0 && y<0){
        //q4
        printf("Q4\n");
    }
    return 0;
}