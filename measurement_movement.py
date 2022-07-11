import xtralien
from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units
from zaber_motion.binary import Device
from zaber_motion.ascii import AllAxes
from zaber_motion import MovementFailedException
from threading import Thread
import time
from zaber.serial import AsciiSerial, AsciiDevice

def func_speed(preset_speed):
    with Connection.open_serial_port("/dev/tty.usbserial-A10JT7DA") as con:
        device_list = con.detect_devices()
        device = device_list[0]
        axis = device.get_axis(1)
        # axis.home()
        speed = axis.settings.get("maxspeed", Units.VELOCITY_MILLIMETRES_PER_SECOND)
        print("Max speed is", speed)
        axis.settings.set("maxspeed", preset_speed, Units.VELOCITY_MILLIMETRES_PER_SECOND)

        # axis.wait_until_idle()
        temperature = axis.settings.get("driver.temperature")
        print(f'Driver temperature {temperature}C')
        temperature = axis.settings.get("driver.temperature")
        return preset_speed


def func_position(preset_position):
    with Connection.open_serial_port("/dev/tty.usbserial-A10JT7DA") as con:
        device_list = con.detect_devices()
        device = device_list[0]
        axis = device.get_axis(1)
        #axis.settings.set("maxspeed", preset_speed, Units.VELOCITY_MILLIMETRES_PER_SECOND)
        axis.move_absolute(preset_position, Units.LENGTH_MILLIMETRES)

def current_position():
    from zaber.serial import AsciiSerial, AsciiDevice
    with Connection.open_serial_port("/dev/tty.usbserial-A10JT7DA") as con:
        device_list = con.detect_devices()
        device = device_list[0]
        axis = device.get_axis(1)

        position = axis.get_position()
        return position

def measurement_function():
    '''Here I am setting the Source_Meausure Unit and execute 100 current measurements @ 0.8 V'''
    with xtralien.Device("/dev/tty.usbmodem141201") as SMU:
        #checking if the SMU is enabled (open the current/voltage source)
        SMU.smu1.set.enabled(True, response=0)
        #setting the voltage - in myh case 0.8 V
        SMU.smu1.set.voltage(0.8, response=0)
        #Here I execute 100 measurements
        data_pass = []
        for i in range(0,100):
            data = SMU.smu1.measurei()
            time.sleep(0.1)
            data_pass.append(data)
        # when finished I turn off the current and voltage source
        SMU.smu1.set.enabled(False, response=0)
        return data_pass
def online_displaying():
    with xtralien.Device("/dev/tty.usbmodem141201") as SMU:
        #checking if the SMU is enabled (open the current/voltage source)
        SMU.smu1.set.enabled(True, response=0)
        #setting the voltage - in myh case 0.8 V
        SMU.smu1.set.voltage(0.8, response=0)
        #Here I execute 100 measurements
        data = SMU.smu1.measurei()
        time.sleep(0.1)
        # when finished I turn off the current and voltage source
        SMU.smu1.set.enabled(False, response=0)
        return data

def main():
    '''Here it is only left because I was testing it'''

    measurement_function()

if __name__ == '__main__':
    main()
    # Thread(target=func1).start()
    # Thread(target=func2).start()