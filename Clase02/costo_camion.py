import csv

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        
        for row in rows:
            cajones = float(row[1])
            precios = float(row[2])
            precio_frutas = cajones * precios
            costo_total += precio_frutas
    
    return costo_total

nombre_archivo = '../Data/camion.csv'
costo_total = costo_camion(nombre_archivo)
print('Costo total es:', costo_total)










