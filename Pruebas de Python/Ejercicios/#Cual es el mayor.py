#Cual es el mayor
a = float (input("Ingrese A: "))
b = float (input("Ingrese B: "))
c = float (input("Ingrese C: "))

if a>b:
    if a>c:
        print (f"{a} es el mayor que es A")

    else:
        print (f"{c} es el mayor que es C")
else:
    if b>c:
        print (f"{b} es el mayor que es B")
    else:
        print (f"{c} es el mayor que es C")