import serial
import time
from time import localtime, strftime
serialPort= serial.Serial('/dev/ttyACM0', 115200, timeout =None)

serialPort.flushInput()
#serialPort.flushOutput()
res =" "
time.sleep(1)
try:
    if serialPort.readable():
        try:
            res = serialPort.readline()
            #print(res)
            res_data = res.decode()[:len(res)-1]
            print(res_data)
            sensor_data = res_data.strip().split(' ')
            print(sensor_data)
            print(len(sensor_data))
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
                        print(sensor_data)
                        print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
        except:
            print("ERROR: No insert Data")
except:
    print("Error: No received Sensor Data")
