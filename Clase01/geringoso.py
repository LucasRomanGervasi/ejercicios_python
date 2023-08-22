#Ejercicio 1.18: Geringoso rústico

#Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

cadena = "cadena"
nueva_cadena= ""

for c in cadena:
    if c.lower() == "a":
        nueva_cadena += c + "pa"
    elif c.lower()  == "e":
        nueva_cadena += c + "pe"
    elif c.lower() == "i":
        nueva_cadena += c + "pi"
    elif c.lower() == "o":
        nueva_cadena += c + "po"
    elif c.lower() == "u":
        nueva_cadena += c + "pu"
    else:
        nueva_cadena += c 
print(nueva_cadena)
