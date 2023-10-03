#Ejercicio 3.5. Función tiene_a()

# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1

# tiene_a('UNSAM 2020')
# tiene_a('abracadabra')
# tiene_a('La novela 1984 de George Orwell')

#Comentario: En su estado actual, la función siempre 
# devuelve True o False después de evaluar el primer carácter 
# de la expresión, sin importar si encuentra o no la letra 'a'. 
# Esto se debe a que el return se encuentra dentro del bucle while, 
# por lo que el bucle se ejecuta solo una vez, independientemente de la longitud de la expresión.



def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a' or expresion[i] == 'A' : #Agrege el or para tambien encontrar las A mayusculas 
            return True
        i += 1 #Sumando i dentro del while recorre toda la plabra
    return False  # Si el bucle termina sin encontrar 'a', devuelve False

# Pruebas
tiene_a('UNSAM 2020')  # Debería devolver False
tiene_a('abracadabra')  # Debería devolver True
tiene_a('La novela 1984 de George Orwell')  # Debería devolver True

#Ejercicio 3.6. Función tiene_a()

# def tiene_a(expresion)
#     n = len(expresion)
#     i = 0
#     while i<n
#         if expresion[i] = 'a'
#             return True
#         i += 1
#     return Falso

# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')

#Comentario: En su estado actual, no se agregaron los dos puntos : al 
# final de la definición de la función def tiene_a(expresion) y tampoco al final del while.
#Se utilizó == en lugar de = para comparar caracteres en la línea if expresion[i] == 'a':.
#Se cambió Falso a False en la línea return False.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#Ejercicio 3.8. Función tiene_uno()

# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene


# tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
# tiene_uno(1984)


def tiene_uno(expresion):
    if isinstance(expresion, (str, int)):
        expresion_str = str(expresion)
        n = len(expresion_str)
        i = 0
        tiene = False
        while (i < n) and not tiene:
            if expresion_str[i] == '1':
                tiene = True
            i += 1
        return tiene
    else:
        return False
    
tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#Comentario: Utilizo una 'isinstance'compruebo si la entrada es una cadena o un número
#Luego convierto expresion en una cadena y asi funciona para ambos casos. 

#Ejercicio 3.8. Función suma()
 
# def suma(a,b):
#     c = a + b

# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")

#Comentario: Hace falta agregarle un return al final de la función

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#Ejercicio 3.9. Función leer_camion()

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion('camion.csv')
# pprint(camion)

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}  # Crear un nuevo diccionario para cada fila
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('camion.csv')
pprint(camion)

#Comentario: El problema del código es que se está utilizando 
# el mismo diccionario registro para cada fila en el bucle for. 
# Esto significa que se está actualizando y agregando entradas al mismo diccionario en cada iteración, 
# y finalmente, todas las filas en camion hacen referencia al mismo diccionario.
#Para solucionar esto agregué un registro = {} para que se vayan acumulando allí
