lista = list(range(1,11))

for i in lista:
    print (i,end="-")

print ("")

Mult = int (input("Multiplado por: "))

for Aux,i in enumerate(lista): #Enumerate sirve para utilizar indices internos
    lista[Aux]*=Mult
    Aux+=1

for i in lista:
    print (i,end="-")