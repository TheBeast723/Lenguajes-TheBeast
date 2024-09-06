/*---------------------------------------
 * Una máquina transmite 80 bits de información binaria
 * encapsulada por el guión 11111101. Se quiere tomar los
 * datos desde el stream asociado al hardware, desechar
 * ambos guiones y colocar en un buffer la información
 * limpia. Para ello se solicita que se realice la
 * simulación del ingreso de datos para probar el
 * software de lectura.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

#define SIZE 10

const char guion=0xfd; //1111 1101


int main() {
	FILE *ptrf=NULL;
	short i,n;
	char g;
	ptrf=fopen("hard","rb");

	fscanf(ptrf,"%c",&g);
	if(g==guion)
		for(i=0;i<SIZE;i++) {
			fscanf(ptrf,"%hd",&n);
			fprintf(stdout,"%hd\n",n);
		}
	else
		puts("Error...");

	fclose(ptrf);
	return 0;
}
