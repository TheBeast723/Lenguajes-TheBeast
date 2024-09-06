/*---------------------------------------
--------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct Nodo{
	char c;
	struct Nodo *n;
}NODO;

int main(){
	NODO *lista=NULL;
	NODO *aux=lista;
	char c;
	while((c=getchar())!='\n'){
		aux=(NODO*)malloc(sizeof(NODO));
		aux->c=c;
		aux->n=lista;
		lista=aux;
	}
	aux=lista;
	while(aux){
		printf("%c ",aux->c);
		aux=aux->n;
	}

	return 0;
}
