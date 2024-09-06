/*---------------------------------------
* Realizaar un programa que permita encontrar
y mostrar el registro de un alumno, ingresando
previamente su número de órden.
--------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


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
	short Max,i=0;
	char res='s';

	FILE *ptrf=NULL;
	ptrf=fopen(name,mode);

	fseek(ptrf,-sizeof(R),SEEK_END);
	fread(&R,sizeof(R),1,ptrf);
	Max=R.Key;
	printf("Cantidad de Registro = %hd\n",Max+1);

	while(res=='s'){
		printf("Ingrese el campo Key del alumno:");
		scanf("%hd",&i);getchar();

		if(i<=Max){
			fseek(ptrf,i*sizeof(R),SEEK_SET);
			fread(&R,sizeof(R),1,ptrf);
			printf("Apellido: %s\n",R.Apellido);
			printf("  Nombre: %s\n",R.Nombre);
		}else
			puts("No existe el Alumno...");


		puts("¿Buscar otro alumnos? (s/n)");
		res=getchar();
	}

	fclose(ptrf);
	return 0;
}

/*
 * printf("\n%hd - %s, %s\n",R.Key,R.Apellido,R.Nombre);
 */
