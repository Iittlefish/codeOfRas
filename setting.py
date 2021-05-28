from singleton import sensorMgr
from classDef import Sensor, Dht22Humi, Dht22Temp, UltraRay
from Protector import protector

sensor = Sensor('firstSensor')
temp = Dht22Temp(4)
humi = Dht22Humi(4)
sensor.setSensor('temp',temp)
sensor.setSensor('humi',humi)
Protector.setTarget('') # input crop variety
