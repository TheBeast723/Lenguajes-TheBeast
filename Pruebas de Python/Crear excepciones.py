from multiprocessing.sharedctypes import Value


def Edad (edad):
    if edad<0:
        raise ValueError ("Edad incorrecta")
    print (edad)

try:
    Edad(-5)

except ValueError as EdadNegativa:
    print (EdadNegativa)