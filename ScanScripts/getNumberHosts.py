import ipcalc
import subprocess
from time import sleep
import os

localIP = os.popen("sudo ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*  netmask ([0-9]*\.){3}[0-9]*' | grep -v '127.0.0\.*' | grep -Eo '([0-9]*\.){3}[0-9]*'").read().split("\n")
NETWORK = str(ipcalc.IP(localIP[0], mask=localIP[1]).guess_network())
SYSTEM_PATH = "/home/pi/SystemScripts/"

subprocess.Popen(["python3", SYSTEM_PATH+"display_number.py", "-1"])
nb_hosts = os.popen("sudo nmap -sn "+NETWORK+" | grep").read()
print(nb_hosts)
subprocess.Popen(["python3", SYSTEM_PATH+"display_number.py", str(nb_hosts)])

sleep(3)
subprocess.Popen(["python3", SYSTEM_PATH+"display_number.py", "-1"])