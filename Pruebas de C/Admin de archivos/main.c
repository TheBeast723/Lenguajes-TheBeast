#include <stdio.h>
#include <stdlib.h>
int main (){
FILE * Archivo;
Archivo = fopen ( "C:\\Users\\ejemplo.txt" ,"wt" );
puts("Ingrese texto");
short c;
getchar ();
while(!feof(stdin)){
		putc(c,Archivo);
		c=getc(stdin);
	}
fclose ( Archivo );
return 0;
}
