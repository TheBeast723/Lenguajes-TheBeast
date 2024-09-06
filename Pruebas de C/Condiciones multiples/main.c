#include <stdio.h>
#include <stdlib.h>

int main (){
    int h,min,seg;

    printf ("Ingrese la hora \n");
    scanf ("%i",&h);

    printf ("Ingrese los minutos \n");
    scanf ("%i",&min);

    printf ("Ingrese los segundos \n");
    scanf ("%i",&seg);

    if (h<=23 && min<=59 && seg<=59)
    {
        seg++;
        switch(seg){
      case 60: min++;seg=0;
      }
      switch(min){
      case 60: min++;min=0;h++;
      }
      switch(h){
      case 24: h=0;min=0;seg=0;
      }
    printf ("La hora ingresada es %i:%i:%i",h,min,seg);
   }
    else{
        printf ("La hora introducida no es valida");
    }
return EXIT_SUCCESS;
}
/*int main(){
    int x,i;

    for (i=0;i<2;i++){

    printf ("Introduce un numero: \n");
    scanf ("%i",&x);

    if (x>1 || x<=10){ //&& añade condiciones que se tienen que cumplir // || 1 de las condiciones tiene que ser cierta
        printf ("El numero se encuentra entre 0 y 10 \n");
        i=2;
    }
    else {
        printf ("El numero no se encuentra entre 0 y 10 \n \n");
    i=0;
    }
    }
    return EXIT_SUCCESS;
}
*/

/*int main (){
    int h,min,seg;

    printf ("Ingrese la hora \n");
    scanf ("%i",&h);

    printf ("Ingrese los minutos \n");
    scanf ("%i",&min);

    printf ("Ingrese los segundos \n");
    scanf ("%i",&seg);

    if (h<=23 && min<=59 && seg<=59)
    {
        seg+=1;
        if (seg==60){
            min+=1;
            seg=0;
        }
        if (min==60){
            h++;
            min=0;
        }
        if (h==24){
            h=0;
            min=0;
            seg=0;
        }
        printf ("La hora ingresada es %i:%i:%i",h,min,seg);
    }
    else{
        printf ("La hora introducida no es valida");
    }
return EXIT_SUCCESS;
*/
