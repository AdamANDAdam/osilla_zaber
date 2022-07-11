import matplotlib.pyplot as plt
import numpy as np
from measurement_movement import online_displaying as data_source



for i in range(50):

    plt.scatter(i,float(data_source()))
    plt.draw()
    plt.pause(0.1)
