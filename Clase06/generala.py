# -*- coding: utf-8 -*-

import numpy as np

import random
def tirar():
    tirada=[]
    for i in range(5):
        dado = random.randint(1,6)
        tirada.append(dado)
    return (tirada)

#tirada1 = tirar(tirada)

def es_generala(tirada):
    generala = False
    if tirada[0] == tirada[1] == tirada[2] == tirada[3] == tirada[4]:
        generala = True
    return generala

#es_generala(tirar(tirada))
#%% Toma un dado de una tirada donde salieron todos numeros diferentes

from collections import Counter

def nueva_tirada(lista):
    juego_nuevo = tirar()
    cantidad_a_tirar = 5 - len(lista)
    dados_validos = juego_nuevo[0:cantidad_a_tirar]         
    return dados_validos


def ver_repetidos(tiro, lista):
    for dado in tiro:
            if dado == lista[0]:
                lista.append(dado)


def generala_no_servida():
    #realizacion de 3 tiradas
    #PRIMER TIRO
    primer_tiro = tirar()
    
    if es_generala(primer_tiro):
        return True
    
    else:
        num, cantidad = Counter(primer_tiro).most_common()[0] 
        lista_repetidos=[num for i in range(cantidad)] 
        
        #SEGUNDO TIRO
        segundo_tiro = nueva_tirada(lista_repetidos)
        ver_repetidos(segundo_tiro, lista_repetidos)
        
        if len(lista_repetidos) == 5:
            return True
        else:
            #TERCER TIRO
            tercer_tiro = nueva_tirada(lista_repetidos)
            ver_repetidos(tercer_tiro, lista_repetidos)
            
            if len(lista_repetidos) == 5:
                return True
        
        return False


def prob_generala(N):    
    G = sum([generala_no_servida() for i in range(N)])
    prob = G/N

    print(f'Tiré {N} veces, de las cuáles {G} saqué generala serivda o no servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida o no en 3 tiros mediante {prob:.3f}.') 
    
prob_generala(1000)
        
#%% 
def nueva_tirada(lista):
   #Determinamos con la resta cuantos datos se van a tirar en la siguiente tirada
   juego_nuevo = tirar()
   cantidad_a_tirar = 5 - len(lista)
   dados_validos = juego_nuevo[0:cantidad_a_tirar]         
   return dados_validos
# Se le pasa una lista de dados para ver cuantos dados le falta para los 5 de la generala

def ver_repetidos(tiro, lista):
    
    for dado in tiro:
            if dado == lista[0]:
                lista.append(dado)
# Busca todos los repetidos y los agrega a una lista 

from collections import Counter
def generala_no_servida2():
    #PRIMER TIRO
    primer_tiro = tirar()
    #print(primer_tiro)
    
    if es_generala(primer_tiro):
        return True
    
    else:
        num, cantidad = Counter(primer_tiro).most_common()[0] 
        #print(num, cantidad)
        lista_repetidos=[num for i in range(cantidad)] 
        #print(lista_repetidos)
        
        if len(lista_repetidos) == 1:
            #SEGUNDO TIRO
            lista_repetidos = [] # Reinicia la lista porque no hay repetidos
            segundo_tiro = tirar() # Osea que mete nuevamente los 5 dados al cubilete y volvemos a buscar repetidos 
            #print(segundo_tiro)
            num, cantidad = Counter(segundo_tiro).most_common()[0] 
            lista_repetidos=[num for i in range(cantidad)]
            #print(lista_repetidos)
            
            if es_generala(segundo_tiro):
                return True
            
        elif len(lista_repetidos) > 1:                             
            #SEGUNDO TIRO
            segundo_tiro = nueva_tirada(lista_repetidos) # En caso de que si halla dados repetidos, simular otra tirada pero solo con el numero de datos de nos devolvio la funcion ver_repetidos
            #print(segundo_tiro)
            ver_repetidos(segundo_tiro, lista_repetidos)
            
            
            if len(lista_repetidos) == 5: #generala en el segundo tiro 
                return True

        #TERCER TIRO
        tercer_tiro = nueva_tirada(lista_repetidos)
        #print(tercer_tiro)
        ver_repetidos(tercer_tiro, lista_repetidos)
        if len(lista_repetidos) == 5: #generala en el tercer tiro
            return True
        
        return False
      
def prob_generala(N):
    G = sum([generala_no_servida2() for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida o no servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida o no servida en 3 tiros mediante {prob:.4f}.')

probabilidad = prob_generala(1000)    

        
        
    
    