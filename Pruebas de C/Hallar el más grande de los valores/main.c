#include <stdio.h>

int main () {

    int a,b,c;

    printf ("Ingrese un valor para A: \n");
    scanf ("%i",&a);

    printf ("Ingrese un valor para B: \n");
    scanf ("%i",&b);

    printf ("Ingrese un valor para C: \n");
    scanf ("%i",&c);

    if (a>b){
        if (a>c){
        printf ("A es el numero mas grande con un valor de %i",a);
                }
    }
    else {
        if (b>c){
            printf ("B es el numero mas grande con un valor de %i",b);
        }
        else {
            printf ("C es el numero mas grande con un valor de %i",c);
        }
    }
return 0;
}
/*
#include <stdio.h>

int main () {

    int a,b,c;

    printf ("Ingrese un valor para A: \n");
    scanf ("%i",&a);

    printf ("Ingrese un valor para B: \n");
    scanf ("%i",&b);

    printf ("Ingrese un valor para C: \n");
    scanf ("%i",&c);

    if (a<b){
        if (a<c){
        printf ("A es el numero mas grande con un valor de %i",a);
                }
    }
    else {
        if (b<c){
            printf ("B es el numero mas grande con un valor de %i",b);
        }
        else {
            printf ("C es el numero mas grande con un valor de %i",c);
        }
    }
return 0;
}
*/
