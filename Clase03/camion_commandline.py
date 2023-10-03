import csv
import sys

def costo_camion(nombre_archivo):
    costo_total = 0.0
    
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        next(filas)
        
        for fila in filas:
            try:
                cajones = int(fila[1])
                precio = float(fila[2])
                costo_total += cajones * precio
            except ValueError:
                print(f'Faltan datos en la línea {filas.line_num} del archivo.')
    
    return costo_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
