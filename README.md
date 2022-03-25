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
```
or 

influxdb
```bash
sudo apt-get install influxdb
sudo apt-get install telegraf
```
https://docs.influxdata.com/telegraf/v1.21/introduction/getting-started/
https://hackmd.io/@0p3Xnj8xQ66lEl0EHA_2RQ/Skoa_phvB
