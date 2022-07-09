import serial
import time
ser = serial.Serial("/dev/ttyUSB0", 9600)


def gps_g():
    ser = serial.Serial("/dev/ttyUSB0", 9600)
    temp = ser.readline()
    if temp.startswith(b'$GNGGA'):
        temp=str(temp)
        temp = temp.split(',')
        #print("temp: " , temp)
        latitude = temp[2]
        #print("latitude:",latitude)
        longitude = temp[4]
        #print("llongitude:",longitude)
        flag = temp[6]
        satellite = temp[7]
        if latitude != '' and longitude != '':
            latitude = int(latitude[0:2]) + (float(latitude[2:8]) / 60)
            longitude = int(longitude[0:3]) + (float(longitude[3:9]) / 60)
            if flag == '1':
                print('當前座標：%s,%s' % (latitude, longitude))
                print('衛星數量：%s' % int(satellite))
                print('定位時間：%s\n' % time.strftime('%Y-%m-%d %H:%M:%S'))
                return float(latitude),float(longitude)
            else:
                print('定位數據無效(%s)' % time.strftime('%Y-%m-%d %H:%M:%S'))
                return 0,0
        else:
            print('定位失敗(%s)' % time.strftime('%Y-%m-%d %H:%M:%S'))
            return 0,0

def gps_t1():
    while True:
        try:
            if gps_g()!=None:
                return int(latitude),int(longitude)

        except:
            pass

