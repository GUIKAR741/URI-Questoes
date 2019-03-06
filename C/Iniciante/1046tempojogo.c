#include <stdio.h>
int main() {
    int horaini,horafim,tempo;
    scanf("%i%i",&horaini,&horafim);
    tempo=horafim-horaini;
    if(tempo<0){
        tempo+=24;
    }
    if(horaini==horafim){
        printf("O JOGO DUROU 24 HORA(S)\n");
    } else printf("O JOGO DUROU %i HORA(S)\n",tempo);
    return 0;
}