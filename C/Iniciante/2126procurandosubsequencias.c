#include <stdio.h>
#include <string.h>
int main(){
    long long int n,m,k=1,j=0,i=0,tn1=0,tn2=0,qtd=0,cont=0,psub=0;
    char n1[110],n2[120];
    while (scanf("%s %s",n1,n2)!=EOF){

//        sprintf(n2,"%lli",m);
        tn1=strlen(n1);
        tn2=strlen(n2);
        qtd=0;
        j=0;
        while (j<tn2) {
            cont=0;
            i=0;
            while (i < tn1) {
                if (n1[i++] == n2[j++]) {
                    cont++;
                    if (n1[i] != n2[j])break;
                }else{
                    break;
                }
                if(j>tn2)break;
            }
            if(cont==tn1){
                psub=j-tn1+1;
                qtd++;
            }
        }
        printf("Caso #%lli:\n",k++);
        if(qtd==0) printf("Nao existe subsequencia\n\n");
        else{
            printf("Qtd.Subsequencias: %lli\n",qtd);
            printf("Pos: %lli\n\n",psub);
        }
    }
    return 0;
}