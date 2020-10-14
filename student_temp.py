import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def calibrate(time, amplitude):

    ##############

    return (((mean(amplitude[len(amplitude)-200:len(amplitude)])-0.88-0.2)/3.62)*8+34)

    #############
