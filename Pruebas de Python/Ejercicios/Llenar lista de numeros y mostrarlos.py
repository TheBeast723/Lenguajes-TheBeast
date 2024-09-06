#lista= list (range(1,51)) Cumple la misma funcion que las lineas 3-6

lista = []

for i in range (1,51):
    lista.append(i)

for i in lista:
    print (f"{i}",end="-")