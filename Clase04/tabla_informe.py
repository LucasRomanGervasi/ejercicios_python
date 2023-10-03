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

print(leer_camion('../Data/camion.csv'))

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

def hacer_informe(camion, precios):
    informe = []
    for fruta in camion:
         nombre = fruta['nombre']
         cajones = fruta['cajones']
         precio_venta = precios.get(nombre, 0.0)
         precio = fruta['precio']
         cambio = precio_venta - precio
         tupla = (nombre, cajones, precio, cambio)
         informe.append(tupla)
    
    return informe

informe = hacer_informe(camion, precios)



# Imprimir el encabezado
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f"{headers[0]:<10s} {headers[1]:<10s} {headers[2]:<10s} {headers[3]:<10s}")
print(f'{"-"*10} {"-"*10} {"-"*10} {"-"*10}')

# Imprimir el informe formateado
for row in informe:
    print(f"{row[0]:<10s} {row[1]:<10d} {row[2]:<10.2f} {row[3]:<10.2f}")
