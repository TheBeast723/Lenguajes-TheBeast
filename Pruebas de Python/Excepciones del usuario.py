from ast import Break
from pickle import TRUE


while True: 
    try: #Hace el intento de ejecutar
        numero = int(input("Numero: "))
        print (f"El numero es : {numero}")

    except: #Se ejecuta si hay un error
        print ("Error")

    else: #Se ejecuta si try funciona correctamente
        print ("Fin del programa sin errores")
        break

    finally: #Se ejecuta siempre haya o no un error
        print ("Programa finalizado")
