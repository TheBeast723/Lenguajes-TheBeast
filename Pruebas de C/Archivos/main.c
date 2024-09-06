/*
Convierta las letras a mayúsculas.
Por último las guarde en un nuevo archivo.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LONGITUD 999999
int main (){
    char Minusculas['\0-1'];
    char Texto[LONGITUD];
    int AuxMin, AuxText;
    FILE * Archivo;
    Archivo = fopen ( "ejemplo.txt" , "wt" ); //Crea el stream
    if (Archivo==NULL){
        printf ("El archivo no existe");
        return -1;
    }
    short c;
    c=getchar();
    while (!feof(stdin)){
    putc(c,Archivo);
    c=getchar();
}
fclose (Archivo);
Archivo = fopen ("ejemplo.txt", "rt");

fgets (Texto, LONGITUD, Archivo);
printf ("%s",Texto);

AuxMin=0;
AuxText=0;

while(Texto[AuxText]!='\0') {


if((Texto[AuxText]>='a' && Texto[AuxText]<='z')) {
Minusculas[AuxMin++]=Texto[AuxText];
}

AuxText++;
}

printf("\nMinusculas: %s \n",Minusculas);

AuxMin=0;
AuxText=0;

while(Texto[AuxText]!='\0') {


if((Texto[AuxText]>='a' && Texto[AuxText]<='z')) {
Minusculas[AuxMin++]=Texto[AuxText];

}

AuxText++;

}

printf ("En mayuscula, seria: %s \n",Minusculas);

return 0;
}
