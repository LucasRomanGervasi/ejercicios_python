#
#Ejercicio 4.3: Un ejemplo pr�ctico de enumerate()
#

import csv

def costo_camion(nombre_archivo):
    f = open (nombre_archivo)
    fila=csv.reader(f)
    next(fila)   #saltea encabezado
    costo_total=0.0
    for col in fila:
        for n_fila, fila in enumerate(fila, start=1):
            
            try:
                costo_total=costo_total+int(fila[1])*float(fila[2])        
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()
    return costo_total

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)
