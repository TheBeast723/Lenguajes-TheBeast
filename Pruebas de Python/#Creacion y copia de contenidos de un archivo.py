#Tarea
#Si no genera los archivos, ejecutar como administrador desde consola usando "python #Tarea.py"

import os

with open ("Archivo.txt","r") as Auxiliar:
    for Linea in Auxiliar:
        res = [char for char in Linea if char.islower()]
        print("Letras en minuscula: ",str(res))
        
Letra= str(res).upper()
print (Letra)

file = open("Copia.txt", "w")
file.write(Letra + os.linesep)
file.close()