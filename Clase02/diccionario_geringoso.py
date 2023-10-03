def geringonzo(original):
    traducida = ""
    for letra in original:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida


def diccionario_geringozo(lista):
    diccionario_geringozo = {}
    for palabra in lista:
        diccionario_geringozo[palabra] = geringonzo(palabra)
    return diccionario_geringozo    

lista= ['banana', 'manzana', 'mandarina']
diccionario = diccionario_geringozo(lista)
print(diccionario)