# -*- coding: utf-8 -*-

import numpy as np

def crear_album(figus_total):
    album_vacio = np.zeros(figus_total, dtype = int)
    return album_vacio

def album_incompleto(A):
    return(0 in A)

def comprar_figu(figus_total):
    figurita = np.random.randint(0, figus_total)    
    return figurita


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cant_figus = 0
    while album_incompleto(album) == True:
        figurita  = comprar_figu(figus_total)
        if album[figurita] == 0: 
            album[figurita] = 1
            cant_figus += 1
        else:
            cant_figus +=1
    return cant_figus

def prob_figus(n):
    figus_total = 6
    F = sum(cuantas_figus(figus_total) for i in range(n))
    prom = F/n
    print(f'Hice {n} repeticiones para completar un album de 6 figuritas y el promedio de figuritas compradas es de {prom}')
    return


def experimento_figus(n_repeticiones, figus_total):
    
    lista = np.array([cuantas_figus(figus_total) for i in range(n_repeticiones)])
       
    prom = np.mean(lista)
    return prom
#%%
import matplotlib.pyplot as plt

def comprar_paquete(figus_total, figus_paquete):
    for i in range(figus_paquete):
        paquete = np.random.randint(0, figus_total, size=figus_paquete)
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cant_paquetes = 0
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:   
            if album[i] == 0: 
                album[i] = 1
            
        cant_paquetes +=1
    return cant_paquetes

def prob_prom_paquete(n_repeticiones, figus_total, figus_paquete):
    
    lista_paquete = np.array([cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)])
    prom = np.mean(lista_paquete)
    return  print(f'Hice {n_repeticiones} repeticiones para completar un album de {figus_total} figuritas y el promedio de paquetes compradas es de {prom}')
        
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete.all:
            album[paquete.pop()-1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")



  