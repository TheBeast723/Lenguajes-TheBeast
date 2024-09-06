#include <stdio.h>

#define MAX 5


int main () {

    int i;
    int arre[MAX];
    int acu=0;
    float prom;

    for (i=0;i<MAX;i++){

        printf ("\Ingrese la nota del alumno %d \n",i+1);
        scanf ("%d",&arre[i]);
        acu=acu+arre[i];
    }
    prom = acu/MAX;

    printf ("\n El promedio es: %5.2f",prom);

    return 0;
}
