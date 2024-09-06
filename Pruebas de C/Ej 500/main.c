/*---------------------------------------
--------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct Nodo{
	int i;
	struct Nodo *n;
	float f;
	char o;
}NODO;

int main(){

	NODO A,B,C;
	NODO * lista=NULL;
	NODO **lis=&lista; // *lis --> lista
	lista = &A; // *lista --> A

	A.n = &B;
	B.n = &C;
	puts("Ingrese 3 enteros...");
	scanf("%d %d %d",&(lista->i),&(lista->n->i),&(lista->n->n->i));
	getchar();
	printf("A.i= %d ",(*lista).i);
	printf("B.i= %d ",(*lis)->n->i);
	printf("C.i= %d ",(**lis).n->n->i);

	return 0;
}
