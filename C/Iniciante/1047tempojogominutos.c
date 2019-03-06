#include <stdio.h>
int main() {
    int horaini,horafim,minutoini,minutofim,tempo,tempomin;
    scanf("%i%i%i%i",&horaini,&minutoini,&horafim,&minutofim);
    tempo=horafim-horaini;
    if(tempo<0){
        tempo+=24;
    }
    tempomin=minutofim-minutoini;
    if(tempomin<0){
        tempomin+=60;
        tempo--;
    }
    if(horaini==horafim && minutoini==minutofim){
        printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)\n");
    } else printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n",tempo,tempomin);
    return 0;
}