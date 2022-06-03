from operator import imod
from influxdb import InfluxDBClient
import time
client = InfluxDBClient('140.128.110.57', 8086, '', '', 'smoke_test1') 
def in_sql(level_value):
    data = [
        {
            "measurement": "smoke_level",
            "tags": {
                "topic": "Sensor/level"
            },
            "fields": {
                "value": level_value
            }
        }
    ]
    data2 = [
        {
            "measurement": "smoke_level",
            "tags": {
                "topic": "Sensor/data"
            },
            "fields": {
                "value": level_value
            }
        }
    ]
    client.write_points(data)

def get_sql():
    result = client.query('select Level from smoke_level') 
    insql_list=list(result.get_points())
    return insql_list
