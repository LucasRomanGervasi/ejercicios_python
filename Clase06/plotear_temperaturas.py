# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas = np.load("../Data/temperaturas.npy")
    plt.hist(temperaturas,bins=25)
    plt.show()
    
    return temperaturas

plotear_temperaturas()
    