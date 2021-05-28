import requests


#PostMan is focus on send post request 
class Postman():

    def send(self,data: dict):
        __url=''                                        # url need to fill in the url of our backend sever  
        __text=None
        __status = None
        __res = requests.post(__url,data)

        __text = __res.text
        __status = __res.status_code
        __reponse={'text':__text,'status':__status}
        
        return __reponse
        

#the device name need to be unique. so we will send request to sever to ensure that the device name is not repeated.
class deviceNameVeri():

    def veriDevice(self,deviceName: str):
        __verification = None                                   #__verification will record the result which verify the device name.
        __reponse = post.send(url,{"deviceName":deviceName})    # and the value of __varification is temporarily set as 0 or 1. 
        __verification = __reponse['text']
        
        return __verification

#sensorMgr manage all snesor in raspberrypi
class SensorMgr():
    __sensorList=[]
    __detectResult={}
    def addSensor(self,sensor):
        self.__sensorList.append(sensor)

    def dectect(self):
        for sensor in self.__sensorList:
            self.__detectResult[sensor.getDeviceName()] = sensor.detect()
        

    def getResult(self):
        return self.__detectResult


post = Postman()
veri = deviceNameVeri()
sensorMgr = sensorMgr()

