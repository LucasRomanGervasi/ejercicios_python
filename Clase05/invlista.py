def invertir_lista(lista):
    invertida = []
    while len(lista) > 0: 
        valor = lista.pop()
        invertida.append(valor)
    return invertida

print(invertir_lista([1,2,3,4]))

print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))