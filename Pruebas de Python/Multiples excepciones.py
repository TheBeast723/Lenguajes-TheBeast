def dividir ():
    while True:
        try:
            num1 = float (input("Primer numero: "))
            num2 = float (input("Segundo numero: "))
            resultado = num1/num2
            print (f"El resultado es: {resultado:.2f}")
        except ValueError:
            print ("Se ingresaron caracteres en vez de numeros")
        except ZeroDivisionError:
            print ("Imposible dividir en 0")
        else:
            print ("Fin del programa")
            break

dividir()