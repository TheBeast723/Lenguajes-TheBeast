#Calcular el área

from importlib import import_module
import math

r = float (input("Ingrese el radio:"))
area = math.pi*r**2
longitud = 2*math.pi*r
print (f"El area es {area:.2f}")
print (f"La longitud es {longitud:.2f}")
