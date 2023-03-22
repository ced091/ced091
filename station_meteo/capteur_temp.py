import smbus2
import bme280
from .models import Bme280

def reading_data():

    port = 1
    address = 0x77
    bus = smbus2.SMBus(port)

    calibration_params = bme280.load_calibration_params(bus, address)

    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)
    # there is a handy string representation too
    #print(data)

    return (data)

def save_data():
    data = reading_data()
    timestamp = float(data.timestamp.timestamp())
    temperature = float(data.temperature)
    pression = float(data.pressure)
    humidity = float(data.humidity)
    point = Bme280(date_point = timestamp, temp = temperature, humidity = humidity, pression = pression)
    point.save()

