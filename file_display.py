import csv

import matplotlib.pyplot as plt
import numpy as np

with open ("measurement.csv", newline='') as measurement:
    reader = csv.reader(measurement)
    arrX = []
    for row in reader:
        arrX.append(row[0].lstrip('['))
        arrX.append(row[0].rstrip(']'))

    # plt.plot(arrX,np.arange(len(arrX)),'o')
    # #plt.xticks('0','0.5','1')
    # plt.ylabel('Current density [mA cm2]')
    # plt.xlabel('Voltage [v]')
    # plt.show()
    for i in range(len(arrX)):
        plt.plot(i,arrX[i],'o')
        plt.draw()
        plt.pause(0.1)
        