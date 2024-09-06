for i in range (2,10):
    if i==8 : 
        continue #Salta lo que hay en el bucle al cumplirse la condicion, funciona en for y while
    print (f"{i}", end=", ")
print ("")

for i in range (2,10):
    if i==8:
        break #Finaliza el bucle al cumplirse la condicion
    print (f"{i}", end=", ")