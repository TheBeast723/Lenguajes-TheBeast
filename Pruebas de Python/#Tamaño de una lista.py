Arr=[1,2,3,4,5,True,[3.14,5.67],"Hola"]
Arr2=[True,False]

print (len(Arr)) #Muestra el tamaño

print(Arr)

Arr.append("Queso") #Agrega el valor siempre al final

print (len(Arr))

print (Arr)

Arr.insert(5,"Seis") #Se dice en cual lugar va, solo sirve para 1 elemento a la vez

print (Arr)

Arr.extend (["Quiero","Yo",69]) #Concatena al final, se declara como lista también

print (Arr)

Arr3 = Arr + Arr2

print (Arr3) #Se suman al igual que valores simples

print ("Seis" in Arr) #Busca un valor en la lista

print (Arr.index("Seis")) #Te dice en cual posicion se encuentra

Arr.append(69)
Arr.append ("Hola")
Arr.append ("Hola")

print (Arr)

print (Arr.count(69)) #Cuenta las veces que se repite un elemento

print (Arr.count("Hola")) #Cuenta las veces que se repite un elemento

Arr.pop(5) #Elimina el ultimo elemento de la lista si se deja en blanco

print (Arr)

Arr.remove("Queso") #Busca y elimina el valor especificado

print (Arr)

Arr.reverse() #Invierte los elementos de la lista

print (Arr)

Arr = Arr*3 #Multiplica los elementos de la lista

print (Arr)
Arr.clear() #Elimina toda la lista

print ("El arreglo quedo como:",Arr)

Arr=[1,5,7,2,8,28,2,7,267,-436,-25,-26]

Arr.sort(reverse=True) #Ordena los elementos de forma descendente, dejar vacío para ascendente

print (Arr)

Arr[0]=8 #Cambia el valor del indice

print (Arr)