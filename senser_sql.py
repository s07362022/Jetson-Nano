from influxdb import InfluxDBClient
import time
client = InfluxDBClient('172.20.10.2', 8086, '', '', 'env_data') 

tem = 23.9
dry = 50.2
light = 600
gps = "12.123.4"
wind = "0"


#DB########################################
def sql(tem,dry,light,gps1,gps2):
    data = [
        {
            "measurement": "env",
            "tags": {
                "topic": "Sensor/env"
            },
            "fields": {
                "tem": tem
            }
        }
    ]
    client.write_points(data)
    data2 = [
        {
            "measurement": "env",
            "tags": {
                "topic": "Sensor/env"
            },
            "fields": {
                "dry": dry
            }
        }
    ]
    client.write_points(data2)
    data3 = [
        {
            "measurement": "env",
            "tags": {
                "topic": "Sensor/env"
            },
            "fields": {
                "light":light 
            }
        }
    ]
    client.write_points(data3)
    data4 = [
        {
            "measurement": "env",
            "tags": {
                "topic": "Sensor/env"
            },
            "fields": {
                "gps": gps1
            }
        }
    ]
    # client.write_points(data4)
    data5 = [
        {
            "measurement": "env",
            "tags": {
                "topic": "Sensor/env"
            },
            "fields": {
                "gps2": gps2
            }
        }
    ]
    # client.write_points(data5)
############db############

#sql(tem,dry,light,gps1,gps2)
#,gps,wind)


#result = client.query('select * from env') 
#print(list(result.get_points())[-1])

