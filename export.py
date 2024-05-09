import time
import requests
import math
import random
import serial
import urllib
import urllib.parse
import threading
import json
TOKEN = ""  # Put your TOKEN here
DEVICE_LABEL = "Arduino"  # Put your device label here
Field1 = ""  # Put your first variable label here
Field2 = ""  # Put your second variable label here

# configure serial port
ser = serial.Serial('COM4', 9600, timeout=1)
print("Reading data from serial port.....");
time.sleep(2)
ser.reset_input_buffer()  # Delete any stale data.

def thingspeak_post(tmp):
    threading.Timer(15,thingspeak_post).start()
    #val=random.randint(1,3)
    URl="https://api.thingspeak.com/update?api_key="
    KEY= '###'
    HEADER='&field1={}&field2={}&field3={}'.format(tmp[0],tmp[1],tmp[2])
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def main():
    # Reading all bytes available bytes till EOL
    line = ser.readline()
    if line:
        rxdata = line.decode()
        print("x= " ,rxdata)
        if ( (rxdata[0]) == "T"):
            
            a = rxdata.split(",")
            tmp =a[1:]
            thingspeak_post(tmp)
            print(tmp)
            print ("Correct")
            print(tmp[0], tmp[1], tmp[2])
            del tmp  # clear received data
            print("Data transfer started")
            print("Data Successfully sent to cloud")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)