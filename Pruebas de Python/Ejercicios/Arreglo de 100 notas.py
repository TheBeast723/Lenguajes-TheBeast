#Realice una aplicación que tras la generación de un arreglo aleatorio de 100 Notas (entre 0 y 10), llame a cuatro funciones diferentes que realizarán las siguientes tareas respectivamente y su resultado será presentado en main.

#a) Devolverá el promedio de las 100 notas.

#b) Devolverá el número de estudiantes aprobados (4 o más).

#c) Devolverá el número de estudiantes reprobados (menos de 4)

#d) Devolverá el promedio de los estudiantes aprobados.

import random

#Variables a utilizar
Total=0
Cont=0
Apr=0
Rep=0
Nota = 0
Aux = 0
PromApr=[]

def promedio (): #Defino el prototipo del promedio de todos los estudiantes
    global Total
    Total+=Nota
    global Cont
    Cont+=1
    return Total,Cont #Retorno las variables a mostrar y utilizar

def Aprobados(): #Defino el prototipo de la cantidad de aprobados
    global Nota
    global Apr
    if Nota>=4:
        Apr+=1
    return Apr

def Reprobados (): #Defino el prototipo de la cantidad de reprobados
    global Nota
    global Rep
    if Nota<4:
        Rep+=1
    return Rep

def PromAprobados(): #Defino el prototipo del promedio de los aprobados
    global Nota
    global Apr
    global Aux
    if Nota>=4:
        Aux+=Nota
    return Aux

for i in range (100):
    Nota = random.randint (0,10)#Generacion de numeros aleatorios
    print (Nota,end="-")
    promedio ()
    Aprobados()
    Reprobados ()
    PromAprobados()
print (f"\nEl promedio es: {Total/Cont:.2f}")
print (f"\nEl total de aprobados es: {Apr}")
print (f"\nEl total de reprobados es: {Rep}")
print (f"\nEl promedio de los aprobados es: {Aux/Cont:.2f}")