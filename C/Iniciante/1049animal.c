#include <stdio.h>
#include <string.h>
int main() {
    char c1[]="vertebrado", c11[]="ave", c12[]="mamifero";
    char c111[]="carnivoro", c112[]="onivoro", c124[]="herbivoro";
    char a1[]="aguia", a2[]="pomba", a3[]="homem", a4[]="vaca";
    char c2[]="invertebrado", c21[]="inseto", c22[]="anelideo";
    char c211[]="hematofago", a5[]="pulga", a6[]="lagarta";
    char a7[]="sanguessuga", a8[]="minhoca";
    char tipo1[22], tipo2[22], tipo3[22];
    scanf("%s", tipo1);
    if(strcmp(tipo1,c1) == 0){
        scanf("%s", tipo2);
        if(strcmp(tipo2,c11) == 0){
            scanf("%s", tipo3);
            if(strcmp(tipo3,c111) == 0){
                printf("%s\n",a1);
            }
            if(strcmp(tipo3,c112) == 0){
                printf("%s\n",a2);
            }
        }else if(strcmp(tipo2,c12) == 0){
            scanf("%s", tipo3);
            if(strcmp(tipo3,c112) == 0){
                printf("%s\n",a3);
            }
            if(strcmp(tipo3,c124) == 0){
                printf("%s\n",a4);
            }
        }
    }if(strcmp(tipo1,c2) == 0){
        scanf("%s", tipo2);
        if(strcmp(tipo2,c21) == 0){
            scanf("%s", tipo3);
            if(strcmp(tipo3,c211) == 0){
                printf("%s\n",a5);
            }
            if(strcmp(tipo3,c124) == 0){
                printf("%s\n",a6);
            }
        }else if(strcmp(tipo2,c22) == 0){
            scanf("%s", tipo3);
            if(strcmp(tipo3,c211) == 0){
                printf("%s\n",a7);
            }
            if(strcmp(tipo3,c112) == 0){
                printf("%s\n",a8);
            }
        }
    }
    return 0;
}