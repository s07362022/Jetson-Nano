## google  
google
```python
import pandas
```


# Jetson-Nano

install cuda 10.2

```bash
sudo apt-get update
```

```bash
sudo apt-get install linux-headers-generic
```

```bash
nano  ~/.bashrc
```
add :
```bash
export CUDA_HOME=/usr/local/cuda-10.2/
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
export PATH=${CUDA_HOME}bin:$PATH
```

```bash
source ~/.bashrc
sudo apt install nvidia-cuda-toolkit
```
or 

influxdb
```bash
# Add warehouse 
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install influxdb
sudo service influxdb start
```
https://docs.influxdata.com/telegraf/v1.21/introduction/getting-started/
https://hackmd.io/@0p3Xnj8xQ66lEl0EHA_2RQ/Skoa_phvB
https://chowdera.com/2022/03/202203100619325549.html

MQTT:
```bash
pip3 install paho-mqtt
```

語音解決方法 :

https://www.devdungeon.com/content/text-speech-python-pyttsx3
