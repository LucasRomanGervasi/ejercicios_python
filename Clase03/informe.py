import csv

def leer_precio(nombre_archivo):
    precios = {}
    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for i, row in enumerate(rows):
            try:
                if row:
                    fruta = row[0]
                    precio = float(row[1])
                    precios[fruta] = precio
            except ValueError:
                print(f'Faltan datos en la línea {i+2} del archivo.')
    
    return precios

def leer_camion(nombre_archivo):
    camion = []
    
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        
        for i, fila in enumerate(filas):
            try:
                if fila:
                    cajon = {
                        'nombre': fila[0],
                        'cajones': int(fila[1]),
                        'precio': float(fila[2])
                    }
                    camion.append(cajon)
                else:
                    print("renglon vacio")
            except ValueError:
                print(f'Faltan datos en la línea {i+2} del archivo.')
    
    return camion

camion = leer_camion('../Data/camion.csv')
precios = leer_precio('../Data/precios.csv')

def venta():
    ventas_local = 0.0
    for fruta in camion:
        nombre_fruta = fruta['nombre']
        if nombre_fruta in precios:
            ventas_local += precios[nombre_fruta] * fruta['cajones']
    return ventas_local

ventas_local = venta()

def costo():
    costo_total = 0.0
    for cajon in camion:
        costo_total += cajon['cajones'] * cajon['precio']
    return costo_total

costo_total = costo()

def balance():
    diferencia = ventas_local - costo_total
    return round(diferencia, 2)

diferencia = balance()

print(f'El costo del camión es: ${costo_total:.2f}')
print(f'Las ventas del local fueron: ${ventas_local:.2f}')
print(f'El balance total es: ${diferencia:.2f}')
