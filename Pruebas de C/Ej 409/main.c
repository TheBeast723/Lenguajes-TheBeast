/*---------------------------------------
* Con la estructura de ejemplo de la teoría
realizar un programa que permita ingresar por teclado
el nombre y apellido de un alumno y se le asigne
de manera automática la posición dentro del
stream en la cual es almacenado para usos futuros.
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
	const char mode[]="w";

	registro R;

	short i=0;
	char res='s';

	FILE *ptrf=NULL;
	ptrf=fopen(name,mode);

	while(res=='s'){

		printf("Ingrese el nombre del alumno:");
		scanf("%s",R.Nombre); getchar();
		printf("Ingrese el nombre del apellido:");
		scanf("%s",R.Apellido); getchar();
		R.Key =i++;

		fwrite(&R,sizeof(R),1,ptrf);

		puts("¿Ingresa otro alumnos? (s/n)");
		res=getchar();
	}

	fclose(ptrf);
	return 0;
}

/*
 * printf("\n%hd - %s, %s\n",R.Key,R.Apellido,R.Nombre);
 */
