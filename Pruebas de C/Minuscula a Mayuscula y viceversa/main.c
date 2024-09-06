#include <stdio.h>
#include <stdlib.h>
int main()
{
    char Minu, Mayu;
    printf("Ingrese una minuscula \n");
    scanf ("%c",&Minu);

    Minu = Minu-32;

    printf ("%c",Minu);

    return 0;
}
