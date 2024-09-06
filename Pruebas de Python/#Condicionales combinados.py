#Condicionales combinados
edad = int (input("Ingrese su edad : "))

if 0<edad<100:
    print ("Correcto")
    if edad>18:
        print ("Mayor de 18")
    else:
        print ("Menor de 18")
else:
    print ("Incorrecto")