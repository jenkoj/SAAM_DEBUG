#!/usr/bin/env python3

import subprocess
import time 
import csv

def read_write_rssi():
    rate = subprocess.check_output('iwconfig wlan0 | grep Bit | cut -b 20-23',shell=True).decode('utf-8').rstrip()
    tx_power = subprocess.check_output('iwconfig wlan0 | grep Bit | cut -b 41-42',shell=True).decode('utf-8').rstrip()
    link = subprocess.check_output('iwconfig wlan0 | grep Link | cut -b 24-25',shell=True).decode('utf-8').rstrip()
    dbm = subprocess.check_output('iwconfig wlan0 | grep Link | cut -b 44-46',shell=True).decode('utf-8').rstrip()
    connection_wan = subprocess.check_output('ping -w 1 8.8.8.8 | grep packet | cut -b 36-38', shell=True).decode('utf-8').rstrip()
    timestamp = round(time.time())

    if connection_wan == "0%":
        status_wan = "up"
    else:
        status_wan = "down"

    if rate == "":
        status_router = "down"
        rate = "0"
        tx_power = "0"
        link = "0"
        dbm = "0"

    else:
        status_router = "up"

    

    with open('rssi.csv', mode='a') as rssi_file:
        entry = csv.writer(rssi_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        entry.writerow([timestamp, rate, tx_power, link, dbm, status_router, status_wan]) 

    print("rate",rate)
    print("tx",tx_power)
    print("link",link)
    print("dbm",dbm)
    print("status wan",status_wan)
    print("status router", status_router)
    print("time",timestamp)

while True:
    
    read_write_rssi()
    time.sleep(60)
