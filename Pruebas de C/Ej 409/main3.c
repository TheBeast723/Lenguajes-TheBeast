/*---------------------------------------
* Recorrer el archivo para buscar el vlor
de un caampo de interés y una vez encontrado
mostrar el apellido y el número de posición.
--------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

typedef struct{
      short dia;
      short mes;
      short anio;
}date;

typedef struct{
      short Key, Nota;
      char Legajo[6], Apellido[20];
      char Nombre[20], Resultado[10];
      char condicion[10];
      date Fecha;
}registro;

int main() {
	const char name[]="archivo1.db";
	const char mode[]="r";
	registro R;

	char n[20];

	FILE *ptrf=NULL;
	ptrf=fopen(name,mode);


	printf("Ingrese el apellido a buscar: ");
	scanf("%s",n); getchar();

	while(fread(&R,sizeof(R),1,ptrf)){
		if(!strcmp(R.Apellido,n)){
			puts("Apellido encontrado.");
			printf("Apellido: %s\n",R.Apellido);
			printf("Posición: %hd\n",R.Key);
		}
	}

	fclose(ptrf);
	return 0;
}

/*
 * printf("\n%hd - %s, %s\n",R.Key,R.Apellido,R.Nombre);
 */
