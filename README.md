# Jetson-Nano

install cuda 10.2

```bash
sudo apt-get update
```

```bash
sudo apt-get install linux-headers-generic
```

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/sbsa/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/sbsa/7fa2af80.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/sbsa/ /"
sudo apt-get update
sudo apt-get -y install cuda
```

or 

