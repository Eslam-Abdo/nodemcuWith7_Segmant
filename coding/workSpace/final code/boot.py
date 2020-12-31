# Complete project details at https://RandomNerdTutorials.com

#we create our web server using sockets and the Python socket API.
try:
  import usocket as socket
except:
  import socket

import uos, machine
try:
  from utime import sleep_ms
except:
  from time import sleep_ms

#The network library allows us to connect the ESP32 or ESP8266 to a Wi-Fi network.
import network

#turn off vendor OS debugging messages
import esp
esp.osdebug(None)

#we run a garbage collector
#A garbage collector is a form of automatic memory management. 
#This is a way to reclaim memory occupied by objects that are no longer in used by the program. 
#This is useful to save space in the flash memory.
import gc
gc.collect()

# hold your network credentials
ssid = 'MicroPython-d6f4e9'
password = 'micropythoN'

#################### Wi-Fi station ################
# To set the ESP8266 as a Wi-Fi station:
#station = network.WLAN(network.STA_IF)
#station.active(True)  #activate the station:
#station.connect(ssid, password) #connects to your router using the SSID and password defined

#################### Acess Point station ################
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)


#The following statement ensures that the code doesn’t proceed while the ESP is not connected to your network
#while station.isconnected() == False:  ##for wifi station##
 # pass
 
while ap.active() == False:
  pass
  
#After a successful connection, print network interface parameters like the ESP32/ESP8266 IP address – use the ifconfig() method   
print('Connection successful')
print(ap.ifconfig())
#print(station.ifconfig())##for wifi station##







