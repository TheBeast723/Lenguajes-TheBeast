#include <stdio.h>
long int factorialrec(long int); // Prototipo
long int y; // Variable global

int main(){

unsigned long int resrecursivo;
    printf ("\t\t App de recursividad\n");
    printf ("Ingrese el valor\n");
    scanf ("%d",&y);
    resrecursivo=factorialrec(y);
    printf ("\n El factorial de %d es %d",y,resrecursivo);
    return 0;
}

long int factorialrec( unsigned long int n)
{
    if (n>0)
        return n*factorialrec(n-1);
    else
        return 1;
}
