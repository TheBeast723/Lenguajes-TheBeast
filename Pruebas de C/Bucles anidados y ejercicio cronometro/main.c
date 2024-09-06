#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <windows.h>
int main()
{
/*int h,min,seg,x;

    x=1000;

    for (h=0;h<24;h++){
        for (min=0;min<60;min++){
            for (seg=0;seg<60;seg++){
                printf ("%02i:%02i:%02i \r",h,min,seg);
                Sleep (x);
            }
        }
    }

    return EXIT_SUCCESS;
}*/
    int a,b,c,d,i,j,k;

    for(i=1;i<10;i++){
        printf ("Tabla del %i \n",i);
        for (j=1;j<=10;j++){
            printf ("%i x %i= %i \n",i,j,i*j);
        }
    }
        return EXIT_SUCCESS;

    }
