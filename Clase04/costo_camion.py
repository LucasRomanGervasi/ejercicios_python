#
#Ejercicio 4.4: La función zip()
#

import csv

def costo_camion(nombre_archivo):
    f = open (nombre_archivo)
    fila=csv.reader(f)
    encabezados = next(fila)   #saltea encabezado
    costo_total=0.0
    for col in fila:
        for n_fila, fila in enumerate(fila, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return costo_total
        
costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)