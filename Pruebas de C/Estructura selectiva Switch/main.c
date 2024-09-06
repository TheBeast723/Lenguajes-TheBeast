#include <stdio.h>
#include <stdlib.h>

int main (void) {
    int a,i;

    for (i=0;i<7;i++){
    printf ("Ingrese un numero entre 1 y 7 \n");
    scanf ("%i",&a);
    switch (a) {
    case 1: printf ("Lunes \n");break;
    case 2: printf ("Martes \n");break;
    case 3: printf ("Miercoles \n");break;
    case 4: printf ("Jueves \n");break;
    case 5: printf ("Viernes \n");break;
    case 6: printf ("Sabado \n");break;
    case 7: printf ("Domingo \n");break;
    default: printf ("Ingrese un numero en el rango asignado \n \n");i=0;
    }
    }
return EXIT_SUCCESS;
}
