import simplejson as json
import numpy as np

from measurement_movement import func2 as osilla

outcome = osilla()
outcome = outcome.tolist()



with open ("measurement.csv", "a", newline='\n') as measurement:
    for i in range(0,len(outcome)):
        measurement.write(str(outcome[i]))
        measurement.write('\n')






