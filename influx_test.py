from influxdb import InfluxDBClient
import time
client = InfluxDBClient('172.20.10.2', 8086, '', '', 'env_data') 

tem = 23.9
dry = 50.2
light = 600
gps = "12.123.4"
wind = "0"


#DB########################################
def sql(tem,dry,light):
    json_body = [
    {
        "measurement": "env",
        "tags": {
            "topic": "Sensor/env"
        },
        #"time":str(datetime.utcnow()),
        "fields": {
            "tem": tem
        }
    },
    {
        "measurement": "env",
        "tags": {
            "topic": "Sensor/env"
        },
        #"time": str(datetime.utcnow()),
        "fields": {
            "dry": dry
        }
    },
    {
        "measurement": "env",
        "tags": {
            "topic": "Sensor/env"
        },
        #"time": str(datetime.utcnow()),
        "fields": {
            "light":light
        }
    }
    ]
    client.write_points(json_body)

#for i in range(15):
    #sql(tem,dry,light,gps1,gps2)
    #client.write_points(json_body)
   
def get_sql():
    result = client.query('select * from env') 
    insql_list=list(result.get_points())
    return insql_list
############db############

#sql(tem,dry,light,gps1,gps2)
#,gps,wind)


#result = client.query('select * from env') 
#print(list(result.get_points())[-1])
