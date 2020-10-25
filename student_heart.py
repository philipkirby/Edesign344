import numpy as np
from statistics import mean

def calibrate(time, amplitude):

    ######################################
    # Enter calibration code here:
    ######################################
    rail = 0
    risingedge = []
    fallingedge = []
    diffrise = []

    i = 0
    k = 1

#edge detection and stamp rising edge times in risiing edge[]
    while  (i < (len(time)-1)) :
        if (amplitude[i] > 4) & (rail == 0):
            if time[i] > 0.05:
                risingedge.append(time[i])
            rail = 1
        if (amplitude[i] < 0.05) & (rail == 1):
            rail = 0

        i = i + 1

    #find difference between rising edge times
    while(k < len(risingedge)):
        diffrise.append(risingedge[k]-risingedge[k-1])
        k = k + 1
    bpm = (1/mean(diffrise))*60



    ######################################

    return round(bpm+0.5)
