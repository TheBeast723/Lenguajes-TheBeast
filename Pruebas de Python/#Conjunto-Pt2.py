#a= set() No es necesario, solamente cuando es un conjunto vacio

a={1,2,3}
b={3,4,5,6}

print (a == b) #Compara los elementos, incluso si el orden es diferente da True

c = a | b #Une los elementos de los conjuntos

print (c)

c= a & b #Dice que numeros hay en la union de ambos conjuntos

print (c)

c= a - b #Diferencia entre los conjuntos, muestra los del A, funciona a la inversa

print (c)

c= a ^ b #Diferencia simétrica, no muestra los elementos en común

print (c)

c.clear()

c= {1,2,3,4,5,6}

print (a.issubset(c)) #A es un subconjunto de C? True, sólo si están todos los elementos

c.clear()

c= {"Hola","Ñoqui"}

print (a.issubset(c)) #A es un subconjunto de C? False

c.clear()

c= {1,2,3,4,5}

print (c.issuperset(a)) #C engloba al conjunto A? True

print (c.issuperset(b)) #C engolba al conjunto B? False

print (a.isdisjoint(b)) #NO comparten algun elemento? False

a.clear()

a= {1,2}

print (a.isdisjoint(b)) #NO comparten algun elemento? True

a=frozenset({1,2}) #No cambia su valor