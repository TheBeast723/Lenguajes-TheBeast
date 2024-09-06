/*---------------------------------------
 * Una máquina transmite 80 bits de caracteres
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
	ptrf=fopen("hard","wb");
	srand(time(NULL));

	fprintf(ptrf,"%c",guion);

	for(i=0;i<SIZE;i++) {
		n=rand()%20;
		fprintf(ptrf,"%d",n);
		printf("%hd",n);
	}
	puts("FIN...");


	fclose(ptrf);
	return 0;
}
