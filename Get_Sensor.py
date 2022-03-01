import serial
import time
import pymysql
from time import localtime, strftime
serialPort= serial.Serial('/dev/ttyUSB0', 115200, timeout =None)
#MySQL MariaDB
conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='espdata') 

serialPort.flushInput()
#serialPort.flushOutput()
res =""
time.sleep(1)
try:
    while serialPort.readable():
        try:
            res = serialPort.readline()
            #print(res)
            res_data = res.decode()[:len(res)-1]
            #print(res_data)
            sensor_data = res_data.strip().split(' ')
            #print(sensor_data)
            #print(len(sensor_data))
            if (sensor_data[0]):
                sid = sensor_data[0].strip()
            else:
                sid = "0"
            if (sensor_data[1]):
                volt = sensor_data[1].strip()
            else:
                volt = "0"
            if (sensor_data[2]):
                voltr=sensor_data[2].strip()
            else:
                voltr="0"
            if (sensor_data[3]):
                curr = sensor_data[3].strip()
            else:
                curr="0"
            if (sensor_data[4]):
                gradx = sensor_data[4].strip()
            else:
                gradx ="0"
            if (sensor_data[5]):
                grady = sensor_data[5].strip()
            else:
                grady="0"
            if (sensor_data[6]):
                humi = sensor_data[6].strip()
            else:
                humi="0"      

            if (sensor_data[7]):
                tempr = sensor_data[7].strip()
            else:
                tempr="0"     

            if (sensor_data[8]):
                tempub = sensor_data[8].strip()
            else:
                tempub="0"
            if (sensor_data[0]) and (len(sensor_data)==9):
                try:
                    queryString = "INSERT INTO esp_data(sid,volt,voltr,curr,gradx,grady,humi,tempr,tempub,time0) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    print(sensor_data, strftime("%Y-%m-%d %H:%M:%S",localtime()))
                        #insert values in SENSORDATA DB
                    with conn.cursor() as cur:
                            cur.execute(queryString,(sid,volt,voltr,curr,gradx,grady,humi,tempr,tempub,strftime("%Y-%m-%d %H:%M:%S",localtime())))
                            conn.commit()
                except:
                        print("Error: No insert Data")        
                        
                        
                        
                        
                        
                        
                        
                        print(sensor_data)
                        print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
        except:
                print("ERROR: No insert Data")
except KeyboardInterrupt:
        exit()
finally:
        conn.close()