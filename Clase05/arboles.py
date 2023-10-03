import csv

#Ejercicio 5.15: Lectura de todos los árboles
arboleda = []
def leer_parque(nombre_archivo):
    
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                if row[7]:
                    arbol = {
                        'nombrecom': row[7],
                        'log': row[0],
                        'lat': row[1],
                        'altura_tot': row[3],
                        'diametro': row[4],
                    }
                    arboleda.append(arbol)
            except ValueError:
                print(f'Faltan datos en la línea {i+2} del archivo.')
    
    return arboleda

nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
arboles_general_paz = leer_parque(nombre_archivo)

#Ejercicio 5.16: Lista de altos de Jacarandá
H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombrecom'] == 'Jacarandá']
print(H) 

#Ejercicio 5.17: Lista de altos y diámetros de Jacarandá
H2 = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombrecom'] == 'Jacarandá']
print(H2)