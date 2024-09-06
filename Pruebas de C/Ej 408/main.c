/*---------------------------------------
* El encabezado comprende cuatro campos.
(00)2 bytes El primero corresponde a la firma, que indica que se trata de un archivo BMP con dos caracteres.
	BM, 424D en hexadecimal, que indica que se trata de un mapa de bits de Windows.
	BA que indica que se trata de un mapa de bits OS/2.
	CI que indica que se trata de un icono de color de OS/2.
	CP indica que es un puntero de color de OS/2.
	IC indica que es un icono de OS/2.
	PT indica que es un puntero de OS/2.
(02)4 bytes el tama�o total del archivo en bytes.
(06)4 bytes es un campo reservado
(10)4 bytes ubicaci�n del inicio de la informaci�n de la imagen en relaci�n con el comienzo del archivo (desajuste)
(14)4 bytes tama�o del encabezado de informaci�n del mapa de bits en bytes.
Los siguientes valores hexadecimales son posibles seg�n el tipo de formato BMP:
	28 para Windows 3.1x, 95, NT;
	0C para OS/2 1.x;
	F0 para OS/2 2.x.
(18)4 bytes ancho de la imagen, n�mero de p�xeles contados de forma horizontal.
(22)4 bytes altura de la imagen, n�mero de p�xeles contados de forma vertical.
(26)2 bytes El n�mero de planos siempre 1.
(28)2 bytes profundidad del color, bits usados para codificar el color(1, 4, 8, 16, 24 o 32)
(30)4 bytes m�todo de compresi�n (en 4 bytes). es 0 cuando la imagen no est� comprimida o 1, 2 o 3 seg�n el tipo de compresi�n usado:
	0 sin compresi�n
	1 para la codificaci�n RLE de 8 bits por p�xel;
	2 para la codificaci�n RLE de 4 bits por p�xel;
	3 para la codificaci�n de campo de bits, lo que significa que el color fue codificado por una m�scara triple representada por la paleta.
(34)4 bytes tama�o total de la imagen en bytes.
(38)4 bytes resoluci�n horizontal, n�mero de p�xeles por metro contado de forma horizontal.
(42)4 bytes resoluci�n vertical, n�mero de p�xeles por metro contado de forma vertical.
(46)4 bytes n�mero de colores de la paleta.
(50)4 bytes n�mero de colores importantes de la paleta. vale 0 cuando todos los colores son importantes.
(54) primer byte
(N) ancho x alto x 3
--------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

typedef unsigned char hBMP [54];


int main() {
	FILE *ptrf=NULL;
	const char name[]="pixel.bmp";
	hBMP Buf;
	unsigned i;

	ptrf = fopen(name,"rb");
	printf("Encabezado de %s\n",name);

	fread(&Buf,2,1,ptrf);
	printf("firma: %c%c\n",Buf[0],Buf[1]);

	fread(&i,sizeof(unsigned),1,ptrf);
	printf("tama�o del archivo: %u[bytes]\n",i);

	fseek(ptrf,18,SEEK_SET);
	fread(&i,sizeof(unsigned),1,ptrf);
	printf("tama�o en x: %u[pixeles]\n",i);
	fread(&i,sizeof(unsigned),1,ptrf);
    printf("tama�o en y: %u[pixeles]\n",i);

	fclose(ptrf);

	return 0;
}
