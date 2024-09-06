#include <stdio.h>
#include <time.h>
#include <math.h>
#define MAX 10
int main(void)
{
    int f,c,suma; //Variables adicionales
    int ent[]={1,2,3,4,5}; //Arreglo bidimensional
    srand(time(NULL)); //Generacion de semilla
    printf("Arreglo bidimensional entre 1 y 100\n\n");

    for (f=0;f<MAX;f++){
        for (c=0; c<MAX;c++){
            ent[f]=rand()%101;
            printf(" %d ",ent[f]); //Muestro el arreglo bidimensional por pantalla de forma matricial
        }
        printf("\n");
    }

   for (int i=0;i<100;i++){
    suma = suma+ent[i];
   }
   printf ("%d",suma);
    return 0;
}
