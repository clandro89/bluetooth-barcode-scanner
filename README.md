# Bluetooth barcode scanner


### Installation

First you need to update your Raspberry Pi
```
sudo apt-get update
```

Then you need to install the packages related to Bluetooth. 
```
sudo apt-get install bluetooth blueman bluez
```

Then install the required dependencies for installing OpenCV on your Raspberry Pi.

```
sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
```

After that, install python dependencies
```
pip install -r requirements.txt
```

Run bluetooth barcode scanner:
```
python main.py
```
