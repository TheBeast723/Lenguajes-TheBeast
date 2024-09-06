Conjunto = set() #Requisito para ser conjunto y no diccionario

Conjunto = {1,2,3,4,5,6.54,7,"Hola",True,"Hola"}  #No puede almacenar una colección dentro de los conjuntos, borra los duplicados

Conjunto.add (15) #Lo agrega donde quiere, son desordenados

print (Conjunto)

Conjunto.discard("Hola") #Elimina el elemento especificado

print (Conjunto)

print ("Hola" not in Conjunto) #Busca un valor en el conjunto

Conjunto.clear() #Vacia el conjunto

print (Conjunto)

