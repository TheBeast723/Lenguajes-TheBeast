*---------------------------------------
* Haciendo uso de las funciones expuestas
* hasta aquí, escribir un archivo prueba.c
* ingresando caracteres desde el teclado y
* finalizar ese ingreso con el carácter EOF.
* Luego mostrar el archivo por stdout.
--------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main() {

	FILE *ptrf=NULL; //Manipulador - file descriptor

	ptrf = fopen("prueba.txt","w+"); // crear el stream

	puts("Ingrese los datos...");
	short c;
	c=getc(stdin);//==>> getchar()

	while(!feof(stdin)){ //ctr+d
		putc(c,ptrf);
		c=getc(stdin);
	}

	rewind(ptrf);

	puts("Archivo:");

	c=getc(ptrf);
	while(!feof(ptrf)){
		putc(c,stdout);
		c=getc(ptrf);
	}

	fflush(ptrf);
	fclose(ptrf);
	return 0;
}
