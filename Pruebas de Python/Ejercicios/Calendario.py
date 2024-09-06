# ICM00794-Fundamentos de Computación - FCNM-ESPOL
# 2Eva_IIT2008_T3 Crear un Calendario
# Propuesta: edelros@espol.edu.ec

import numpy

dprimer = int(input('¿día de inicio del mes?: '))
diasmes = int(input('¿días del mes?: '))

# El calendario vacío al inicio
calendario = np.zeros(shape=(6,7), dtype=int)
c = dprimer - 1
f = 0
dia = 1
while (f<=5 and dia<=diasmes):
    while (c<=6 and dia<=diasmes):
        calendario[f,c] = dia
        dia = dia + 1
        c = c + 1
    f = f + 1
    c = 0

print('   D  L  M  M  J  V  S')
print(calendario)
# Tarea: Validar primer día del mes entre 1 y 7, 
#    y número de días del mes entre