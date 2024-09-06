numero = int (input ("Ingrese un numero: "))
numero2 = int (input("Ingrese otro numero: "))

if numero%2==0 and numero2%2==0:
   print ("Ambos son pares")
elif numero%2==0 and numero2%2!=0:
    print ("Solo el 1er numero es par")
elif numero%2!=0 and numero2%2==0:
    print ("Solo el 2do numero es par")
else:
    print ("Ninguno es par")