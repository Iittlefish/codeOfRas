import post, sensorMgr from singleton
import schedule
import protector from Protector

result = sensorMgr.getResult()
schedule.every(2).minute.do(post.send(result))

while True:
    sensorMgr.dectect()
    protector.dectectRisk()
    protector.protect()
    schedule.run_pending()
