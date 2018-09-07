from grovepi import *
from grove_rgb_lcd import *
import time
import smbus
import RPi.GPIO as GPIO
from grove_i2c_barometic_sensor_BMP180 import BMP085


class WeatherStation(object):
    def __init__(self, port=7):
        self.dht_sensor_port = port
        setRGB(0,255,0)

    def get(self):    

        try:
            temp, hum = dht(self.dht_sensor_port, 0)
            # Get the temperature and Humidity from the DHT sensor
            
            t = str(temp)
            h = str(hum)
            print("Temp:" + t + "C      " + "Humidity :" + h + "%")
            setText("Temp:" + t + "C      " + "Humidity :" + h + "%")
            return t, h
        except (IOError, TypeError) as e:
            print "Error"


class Barometer(object):
    def __init__(self, mode=1):
        print ("a")
        # Initialise the BMP085 and use STANDARD mode (default value)
        # bmp = BMP085(0x77, debug=True)
        self.bmp = BMP085(0x77, mode)

        # To specify a different operating mode, uncomment one of the following:
        # bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
        # bmp = BMP085(0x77, 1)  # STANDARD Mode
        # bmp = BMP085(0x77, 2)  # HIRES Mode
        # bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

        rev = GPIO.RPI_REVISION
        if rev == 2 or rev == 3:
            bus = smbus.SMBus(1)
        else:
            bus = smbus.SMBus(0)

    def get(self):
        try:
            print ("a")
            temp =self.bmp.readTemperature()

            print ("b")            
            # Read the current barometric pressure level
            pressure = self.bmp.readPressure()/100.0

            # To calculate altitude based on an estimated mean sea level pressure
            # (1013.25 hPa) call the function as follows, but this will not be very accurate
            # altitude = bmp.readAltitude()

            # To specify a more accurate altitude, enter the correct mean sea level
            # pressure level.  For example, if the current pressure level is 1023.50 hPa
            # enter 102350 since we include two decimal places in the integer value
            print ("c")
            altitude = self.bmp.readAltitude(101560)

            print("Temperature: %.2f C" % temp)
            print("Pressure:    %.2f hPa" % pressure)
            print("Altitude:    %.2f m" % altitude)

            return temp, pressure, altitude

        except Exception as e:
            pass
            

barometer= Barometer()    
# station= WeatherStation()

while True:
    time.sleep(2)
    # print(station.get())
    print(barometer.get())
