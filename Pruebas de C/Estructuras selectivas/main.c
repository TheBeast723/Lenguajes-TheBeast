#include <stdio.h>

int main () {

    int x;

    printf ("Ingrese un valor para x: \n");
    scanf ("%i",&x);

    if (x>=5){

        printf ("El valor de x es igual a %i \n",x);
    }
    else{
        printf ("El valor es ingresado es menor que 5, que es %i",x);
    }
return 0;
}
