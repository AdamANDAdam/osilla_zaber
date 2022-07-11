import csv
import math
import simplejson as json
import numpy as np
import matplotlib.pyplot as plt

from measurement_movement import func2 as osilla

outcome = osilla()
outcome = outcome.tolist()



with open ("measurement.csv", "a", newline='\n') as measurement:
    for i in range(0,len(outcome)):
        measurement.write(str(outcome[i]))
        measurement.write('\n')



with open ("measurement.csv", newline='') as measurement:
    reader = csv.reader(measurement)
    arrX,arrY = [],[]
    x_label = [0, 0.25, 0.5, 0.75, 1, 1.25]
    for row in reader:
        arrX.append(row[0].lstrip('['))
        arrY.append(row[1].rstrip(']'))

    plt.plot(arrX,arrY,'o')
    #plt.xticks('0','0.5','1')
    plt.ylabel('Current density [mA cm2]')
    plt.xlabel('Voltage [v]')
    plt.show()



