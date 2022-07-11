#Here is the module for saving the data and displaying it later on

from measurement_movement import measurement_function as osilla

def main():
    outcome = osilla()

    with open ("measurement.csv", "a", newline='\n') as measurement:
        for i in range(0,len(outcome)):
            measurement.write(str(outcome[i]))
            measurement.write('\n')
main()



