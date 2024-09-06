#include <stdio.h>
#include <stdlib.h>

int main()
{
    char a;

    do{
        printf ("Presione la letra s \n");
        fflush (stdin);
        scanf ("%c",&a);
    }while(a!='s'&& a!='S');
    return EXIT_SUCCESS;
}
/*
int main()
{
    int a,b,i;
    do{
        printf ("Ingrese el 1er rango de numeros: \n");
    scanf ("%i",&a);

        printf ("Ingrese el 2do rango de numeros: \n");
    scanf ("%i",&b);

    }while (a>b);
    printf ("Los numeros comprendidos entre %i y %i son: \n",a,b);

    i=a;
    i++;
    do{
        printf ("%i, ",i);
        i++;
    }while (i<b);

    return EXIT_SUCCESS;
}
*/
