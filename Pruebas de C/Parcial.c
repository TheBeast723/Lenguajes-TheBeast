#include <stdio.h>
#include <time.h>
#include <math.h>
#define MAX 20
int main(void)
{

    int i,f,c,first; //Variables adicionales
    char ent[MAX][MAX]; //Arreglo bidimensional
    char s1[10]; //Segundo arreglo
    srand(time(NULL)); //Generacion de semilla
    printf("Arreglo bidimensional entre L y T mayusculas\n\n");

    for(f=0; f<MAX; f++)
    {
        for(c=0; c<MAX; c++)
        {
            ent[f][c]='L'+rand()%9;
            printf(" %2c ",ent[f][c]); //Muestro el arreglo bidimensional por pantalla de forma matricial
        }
        printf("\n");
    }

    printf("\n");

    printf("Segundo arreglo con caracteres aleatorios \n\n");

    puts(s1);

    return 0;
}
