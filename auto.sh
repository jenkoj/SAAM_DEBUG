#!/bin/bash

cd &&
cd SAAM_DEBUG &&
cp saam-logger.service /lib/systemd/system/ &&
chmod +x rssi_logger.py &&
systemctl enable saam-logger.service &&
systemctl start saam-logger.service