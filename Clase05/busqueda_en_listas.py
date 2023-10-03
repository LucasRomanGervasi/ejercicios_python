def maximo(lista):
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e 
    return m

print(maximo([1,2,7,2,3,4]))

#Versión mejorada

def maximo2(lista):
    m = lista[0]
    for e in lista:
        if e > m:
            m = e
    return m

print(maximo2([-1,-2]))

