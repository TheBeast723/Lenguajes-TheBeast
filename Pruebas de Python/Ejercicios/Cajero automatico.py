a= float (1000)

print (f"Ceunta con un saldo total de {a}")
print ("1. Ingreso")
print ("2. Retiro")
print ("3. Muetsra")
print ("4. Salir")
b= int (input("Escriba "))
if b==1:
    c=float(input("Ingrese el monto a depositar "))
    a += c
    print (f"El monto actual es de {a}")
elif b == 2:
    c= float (input("Ingrese el monto a retirar "))
    if c>a:
        print ("No hay")
    else:
        a -= c
        print (f"El monto actual es de {a}")
elif b == 3:
    print (f"Usted tiene {a} en su cuenta")
else:
    print ("Incorrecto")