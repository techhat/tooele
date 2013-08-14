#!/usr/bin/python2

import bluetooth
import bluetooth._bluetooth as _bt
devices = bluetooth.discover_devices(lookup_names=True)
port = 0x1001
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
sock.connect((devices[0][0], port))
sock.send('01 0D \r')
sock.recv(1024)

