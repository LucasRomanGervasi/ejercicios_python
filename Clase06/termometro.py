# -*- coding: utf-8 -*-

import random
import numpy as np
def medir_temp(n):
    mediciones = []
    for i in range(n):
        grados = random.normalvariate(0,0.2)
        temperatura = 37.5 + grados
        mediciones.append(temperatura)
    
    temp_final = np.array(mediciones)
    np.save("../Data/temperaturas.npy", temp_final)
    return temp_final
   
        
medir_temp(999)
        