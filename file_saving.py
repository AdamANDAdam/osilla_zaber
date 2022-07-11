#Here is the module for saving the data and displaying it later on

from measurement_movement import measurement_function as osilla

outcome = osilla()
outcome = outcome.tolist()



with open ("measurement.csv", "a", newline='\n') as measurement:
    for i in range(0,len(outcome)):
        measurement.write(str(outcome[i]))
        measurement.write('\n')






