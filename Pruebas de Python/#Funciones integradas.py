#Funciones integradas

from tkinter import N


n= int("10")

print (n)
print (type(n))

n= float("10.3")

print (n)
print (type(n))

n= str("10.3")

print (n)
print (type(n))

n=bin (10)
#Lo transforma en binario
print(n)
print (type(n))

n=hex(10)
#Lo transforma en hexadecimal
print (n)
print (type(n))

n=int("0b1010",2)#Hay que especificar la base
#Lo transforma de binario a decimal
print (n)
print (type(n))

n=int ("0xa",16)
#Lo transforma de hexadecimal a decimal
print (n)
print (type(n))

n=abs(-8)
#Completamente innecesario el valor absoluto
print (n)
print (type(n))

n=round(5.61)
#Redonde al valor más cercano
print (n)
print (type(n))

n=len("Angel")#Cuenta los caracteres de una cadena
print (n)
print (type(n))