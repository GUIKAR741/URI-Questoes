#include <stdio.h>
int main() {
    int n,i;
    double x,y,z;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        scanf("%lf%lf%lf",&x,&y,&z);
        printf("%.1lf\n",(x*2+y*3+z*5)/10);
    }
    return 0;
}