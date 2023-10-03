def buscar_precio(fruta):
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
            row = line.strip().split(',')
            if row[0] == fruta:
                precio = row[1]
                print(f"El precio de {fruta} es {precio}")

buscar_precio('Naranja')