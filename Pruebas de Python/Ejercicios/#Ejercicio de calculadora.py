Operacion = input ("Ingrese la operación a realizar: \n S,s: Suma \n R,r: Resta \n M,m: Multiplicación \n D,d: División: \n").lower()

if Operacion=="s":
    num1 = float (input("Ingrese el 1er valor a sumar: "))
    num2 = float (input("Ingrese el 2do valor a sumar: "))
    resultado = num1+num2
    print (f"El resultado es: {resultado:.2f}")

elif Operacion =="r":
    num1 = float (input("Ingrese el 1er valor a restar: "))
    num2 = float (input("Ingrese el 2do valor a restar: "))
    resultado = num1-num2
    print (f"El resultado es: {resultado:.2f}")

elif Operacion =="m":
    num1 = float (input("Ingrese el 1er valor a multiplicar: "))
    num2 = float (input("Ingrese el 2do valor a multiplicar: "))
    resultado = num1*num2
    print (f"El resultado es: {resultado:.2f}")

elif Operacion == "d":
    num1 = float (input("Ingrese el 1er valor a dividir: "))
    num2 = float (input("Ingrese el 2do valor a dividir: "))
    resultado = num1/num2
    print (f"El resultado es: {resultado:.2f}")
    
else:
    print ("No es una operación válida")