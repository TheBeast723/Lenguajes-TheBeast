letra = input ("Ingrese una letra: ").lower()

#palabra = letra.lower(palabra) devuelve una copia que se almacena en "palabra"

#letra = input ("Ingrese una letra: ").upper() transforma en mayuscula, misma sintaxis que el anterior

if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print ("Es una vocal")
else:
    print ("Es una consonante")