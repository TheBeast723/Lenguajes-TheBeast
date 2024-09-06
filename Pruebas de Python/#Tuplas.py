Tupla = (4,"Hola",3.,14,True,4) #Los valores de una tupla no cambian

print (Tupla[1]) #Muestra elementos igual que una lista

print ("Hola" in Tupla) #Permite la busqueda

print (Tupla.index("Hola")) #También el índice

print (Tupla.count(4)) #También contar

print (len(Tupla)) #Ver el tamaño

Arr =list (Tupla) #Le damos a la lista el valor de la tupla

print ("Esto es una lista",Arr)

print ("Esto es una tupla",Tupla)

Arr = [1,2,3,4,5,6]

Tupla =tuple (Arr) #Le damos a la tupla el valor de la lista

print (Tupla)