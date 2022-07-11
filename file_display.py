import csv

import matplotlib.pyplot as plt
import numpy as np

def file_disp():
    with open('measurement.csv', newline='') as f:
        reader = csv.reader(f)
        list(reader)
        for row in reader:

            print(', '.join(row))
            plt.scatter(row)
            plt.pause(0.1)
            plt.draw()

            break


        # plt.plot(arrX,np.arange(len(arrX)),'o')
        # #plt.xticks('0','0.5','1')
        # plt.ylabel('Current density [mA cm2]')
        # plt.xlabel('Voltage [v]')
        # plt.show()
        # for i in range(len(arrX)):
        #     plt.plot(i,arrX[i],'o')
        #     plt.draw()
        #     plt.pause(0.1)
file_disp()