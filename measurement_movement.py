import xtralien
from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units
from zaber_motion.binary import Device
from zaber_motion.ascii import AllAxes
from zaber_motion import MovementFailedException
from threading import Thread
import time

def func1(position):
    with Connection.open_serial_port("/dev/tty.usbserial-A10JT7DA") as con:
        device_list = con.detect_devices()
        device = device_list[0]
        axis = device.get_axis(1)
        # axis.home()
        speed = axis.settings.get("maxspeed", Units.VELOCITY_MILLIMETRES_PER_SECOND)
        print("Max speed is", speed)
        axis.settings.set("maxspeed", 40, Units.VELOCITY_MILLIMETRES_PER_SECOND)

        # axis.wait_until_idle()
        temperature = axis.settings.get("driver.temperature")
        print(f'Driver temperature {temperature}C')
        print('###################################')
        print('###################################')
        print('###################################')
        print('###################################')
        temperature = axis.settings.get("driver.temperature")
        axis.move_absolute(position, Units.LENGTH_MILLIMETRES)


def func2():
    with xtralien.Device("/dev/tty.usbmodem141201") as SMU:
        SMU.smu1.set.enabled(True, response=0)
        volt = []
        curr = []
        SMU.smu1.set.voltage(0.8, response=0)
        for i in range(0,1000):
            data = SMU.smu1.measurei()
            time.sleep(0.1)
            print(data*1000)
            #print(voltage, current)









        SMU.smu1.set.enabled(False, response=0)
def main():
    func1(0)
    func2()


if __name__ == '__main__':
    main()
    # Thread(target=func1).start()
    # Thread(target=func2).start()