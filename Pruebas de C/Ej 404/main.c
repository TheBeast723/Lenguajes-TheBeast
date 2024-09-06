/*---------------------------------------
 * El diseñador definió cada entrada de un script
 * para un procesamiento catch, con lineas de
 * caracteres que deben ser interpretadas como:
 * comandos, mensajes y valores.
 * Los comandos comienzan con @ y 8 caracteres alfanuméricos
 * Los mensajes de 32 caracteres finaliza con \n
 * El script finaliza con .
 * Realizar un programa que permita ingresar el
 * script.
 * Homework
 * programa que permita leerlo e identificar cada linea.
--------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

#define SIZE 34

int main() {
	FILE *ptrf=NULL;
	char buf[SIZE];

	ptrf=fopen("script","r");

	while(!feof(ptrf)){
		buf[0]=getc(ptrf);
		if(buf[0]=='@')
			fgets(&buf[1],9,ptrf);
		else
			fgets(&buf[1],33,ptrf);

		fputs(buf,stdout);
	}
	fclose(ptrf);
	return 0;
}

/* ERRORES
 *
 * Si se lee un comando de 8 caracteres
 * (o un mensaje de 32) no se lee \0
 *
 * cuando se muestra el archivo
 * se repita la última linea de entrada
 * que es inexistente. (vea el archivo
 * con un editor de texto)
 */
