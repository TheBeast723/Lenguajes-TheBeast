#include <stdio.h>
#include <time.h>
float Promedio(float); //Protoripo de promedio
float PromedioApr(); //Prototipo de promedio Aprobados
int Aprobados(); //Prototipo de aprobados
int Desaprobados(); //Prototipo de desaprobador
int SuperanEl4,MenorA4;
int AprList = 0;//Variable auxiliar
int DesList = 0;//Variable auxiliar
int Cal[100];//Arreglo de notas
float Contador = 0;//Variable auxiliar

int main()
{
    int num = 0;//Variable auxiliar
	srand(time(NULL));//Generacion de semilla
    system ("color 04");
	for (int i=0; i<100;i++) {
		Cal[i]=rand()%11; //Ingreso de valores en el arreglo
	}
        printf ("Listado de notas: \n\n");
	for (int i = 0; i < 100; i++) {//Muestreo del arreglo
            if (num+1==100){
                if (num+1<10){
                if (Cal[i]<10){
            printf("Nota numero 0%d:0%d\n",num+1,Cal[i]);
		}
		else{
            printf("Nota numero 0%d:%d\n",num+1,Cal[i]);
        }

            }
		else{
            if (Cal[i]<10){
            printf("Nota numero %d:0%d\n",num+1,Cal[i]);
		}
		else{
            printf("Nota numero %d:%d\n",num+1,Cal[i]);
        }
		}
            }
        else{
            if (num+1<10){
                if (Cal[i]<10){
            printf("Nota numero 0%d: 0%d\n",num+1,Cal[i]);
		}
		else{
            printf("Nota numero 0%d: %d\n",num+1,Cal[i]);
        }

            }
		else{
            if (Cal[i]<10){
            printf("Nota numero %d: 0%d\n",num+1,Cal[i]);
		}
		else{
            printf("Nota numero %d: %d\n",num+1,Cal[i]);
        }
		}
        }
		num++;
	}
	printf("\n\nEl promedio de notas es: %.2f",Promedio(Contador));
	printf("\n\nHay %d estudiantes aprobados",Aprobados());
	printf("\n\nHay %d estudiantes reprobados",Desaprobados());
	printf("\n\nEl promedio de los aprobados es %.2f\n",PromedioApr());
	printf ("\n\n                                       Sosa Ruiz Angel Alexis-43477698-EISI879\n\n");
	system ("pause");
}

float Promedio(float Contador) {//Calcula el promedio
	for (int i=0; i<100; i++) {
		Contador+=Cal[i];
	}
	float Media=Contador/100;
	return Media;
}

int Aprobados() {//Calcula los aprobados
	for (int i=0; i<100; i++) {
		if (Cal[i]>=4) {
			SuperanEl4++;
		}
	}
	return SuperanEl4;
}

int Desaprobados() {//Calcula los desaprobados
	for (int i=0; i<100; i++) {
		if (Cal[i]<4) {
			MenorA4++;
		}
	}
	return MenorA4;
}

float PromedioApr() {//Calcula el promedio de aprobados
	for (int i=0; i<100; i++) {
		if (Cal[i]>=4) {
			AprList+=Cal[i];
		}
	}
	float Media=(float)AprList/SuperanEl4;
	return Media;
}
