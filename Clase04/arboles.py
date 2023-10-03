import csv

parque = 'GENERAL PAZ'
def leer_parque(nombre_archivo, parque):
    arboles = []
    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                if row[10] == parque:
                    arbol = {
                        'log': row[0],
                        'lat': row[1],
                        'altura total': row[3],
                        'diametro': row[4],
                        'nombre completo': row[7]
                    }
                    arboles.append(arbol) #NO PUDE IMPLEMENTAR ZIP().
            except ValueError:
                print(f'Faltan datos en la línea {i+2} del archivo.')
    
    return arboles


nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
arboles_general_paz = leer_parque(nombre_archivo, parque)
print(arboles_general_paz)


print(f"Árboles en el parque {parque}: {len(arboles_general_paz)}")
