def doblar (numero):
    return numero*2

n= 5
n = doblar(n)

print (n)

def valores (numeros):
    for i,j in enumerate (numeros):
        numeros[i]*=2

j=[5,15,23,56]
#valores(j) Modifica el conjunto
valores(j[:]) #No modifica el conjunto

print (j)
