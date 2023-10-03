def propagar(lista):
    n = len(lista)
    resultado = lista.copy()
    for i in range(n):
        if lista[i] == 1:
            j = i - 1
            while j >= 0 and lista[j] == 0:
                resultado[j] = 1
                j -= 1
            j = i + 1
            while j < n and lista[j] == 0:
                resultado[j] = 1
                j += 1

    return resultado

print(propagar([ 0, 0, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))