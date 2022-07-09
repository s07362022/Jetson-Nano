import dht_test as dht02
import bh1750 as bh1
import time
import gps_t
import influx_test
import sql_01
while True:
    temperature, humidity=dht02.dht01()
    time.sleep(2) 
    lightLevel=bh1.bh175001()
    #print(lightLevel)
    time.sleep(2)
    try:
        gps_f,gps_l=gps_t.gps_g()
        print("x:",gps_f,gps_l)
        sql_01.in_sql(gps_f,gps_l)

    except:
        gps_f,gps_l=0,0
    influx_test.sql(temperature, humidity,lightLevel)#,gps_f,gps_l)
    
