import pandas as pd 
import post from singleton
df = pd.read_csv('./data.csv',index_col = "variety")


#the coupling of this class is pretty high. i will continue to optimiz it.
class Protector() :
    __tempUp = __row.tempUp
    __tempLo = __row.tempLo
    __humiUp = __row.humiUp
    __humiLo = __row.humiLo

    def setTarget(self,target):
        self.__target = target
        self.__row = df.loc[target]
        

    def detectRisk(self,sensorDetect):
        tl = 0
        tu = 0
        hl = 0
        hu = 0
        for deviceName in sensorDetect:
            for sensor , value in sensorDetect[deviceName]:
                if sensor == 'temp':
                    if value > self.__tempUp:
                        tu = 1
                    if value < self.__tempLo:
                        tl = 1
                else :self.__
                    if value > self.__humiUp:
                        hu = 1
                    if value < self.__humiLo:
                        hl = 1
        
        self.__envStatus=[tl,tu,hl,hu]

    def protect(self):
        __beProtected = 0
        if __beProtected = 0:
            if self.__envStatus == [0,0,0,0]:
                return __action
            else:
                __beProtected = 1
                __action=''
                __actioncount =0
                if (self.__envStatus[3]==1):
                    __action += '排水'
                    __actioncount += 1
                if ((self.__envStatus[0]+1=) or  (self.__envStatus[0]==1 and self.__envStatus[1] != 1)):
                    if __actioncount !=0:
                        __action += '及灑水'
                    else :
                        __action += '灑水'
                if ((self.__envStatus[1]==1) or (self.__envStatus[0]!=1 and self.__envStatus[3]==0):
                    if __actioncount !=0:
                        __action += '及通風'
                    else :
                        __action += '通風'
                if (self.__envStatus[0]==1):
                    if __actioncount !=0:
                        __action += '及加溫'
                    else :
                        __action += '加溫'

                __req ={'protectAction':__action}
                __status = self.__envStatus
                post.send(__req)
        else:
            __beProtected = 0
            volueRange = [self.__tempLo+2,self.__tempUp-2,self.__humiLo+2,self.__humiUp-2]
            if status[0] ==1:
                if status[0] < volueRange[0] :
                    __bePprotected =1
            if status[1] ==1:
                if status[1] > volueRange[1]:
                    __bePprotected =1
            if status[2] ==1:
                if status[2] < volueRange[2] :
                    __bePprotected =1
            if status[3] ==1:
                if status[3] > volueRange[3]:
                    __bePprotected =1
            
            




                

protector = Protector()
