from abc import ABC 
from abc import abstractmethod
from singleton import post ,veri
import Adafruit_DHT
import time
import random

    

class GPIODevice():
    def __init__(self, pin:int):
        self.__pin = pin
    
    def getPin(self):
        return self.__pin

    @abstractmethod
    def getSensorData(self):
        pass
        return self.__sensorData

class Dht22Temp(GPIODevice):
    def __init__(self,pin):
        super().__init__(pin)
        self.__pin = super().getPin() 
    
    __sensor = Adafruit_DHT.DHT22

    def getSensorData(self):
        __dht22Data = Adafruit_DHT.read_retry(self.__sensor,self.__pin)
        __sensorData = __dht22Data[1]
        __sensorData = round(__sensorData,4)
        return __sensorData
        

class Dht22Humi(GPIODevice):
    def __init__(self,pin):
        super().__init__(pin)
        self.__pin = super().getPin() 
    
    __sensor = Adafruit_DHT.DHT22

    def getSensorData(self):
        __dht22Data = Adafruit_DHT.read_retry(self.__sensor,self.__pin)
        __sensorData = __dht22Data[0]
        __sensorData = round(__sensorData,4)
        return __sensorData

#it's fake sensor.
class UltraRay(GPIODevice):
    random.seed(time.time())
    __ultra=random.random(20.0,60.0)
    def getSensorData(self):
        random.seed(time.time())
        self.__ultra += random.random(-0.00003,0.00003)
        return self.__ultra

class Sensor():
    __sensorDict={}
    def __init__(self, deviceName:str):
    #    if veri.veriDevice(deviceName) != 1:                   #if the device name is repeated, sensor object will delet by itself.
    #        del self
    #        break
        self.__deviceName = deviceName   

    def setSensor(self,sensorName,sensor):
        self.__sensorDict[sensorName] = sensor
    
    def detect(self):
        __dectecResult={}
        for __key, __value in self.__sensorDict.items():    
            __detectResult[__key] = __value.getSensorData()
        return __detectResult

    def getDeviceName(self):
        return  self.__deviceName
    
   


    





sensor = Sensor()
humi = dht22Humi(4)
temp = dht22Temp(4)

sensor.setSensor('temp', temp)
sensor.setSensor('humi', humi)
i=0
while i<20:
   sensor.detect()
   i+=1


