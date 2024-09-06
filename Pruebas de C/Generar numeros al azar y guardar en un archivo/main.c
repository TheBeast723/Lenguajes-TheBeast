#include <stdio.h>
#include <time.h>
#include <math.h>

int main(void)
{
    srand(time(NULL));
    FILE * pf=NULL;
    int i;
    srand(time(NULL));
    i='0'+rand()%9;
    printf ("%s",i);

    return 0;
}
