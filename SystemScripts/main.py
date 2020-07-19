#! /usr/bin/python3

# /etc/init.d/main.py
### BEGIN INIT INFO
# Provides:          main.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

# Main script running all the time, and handeling events as :
	# - launching scans
	# - shutdown the machine

#importing libraries
import RPi.GPIO as GPIO
from time import sleep
import subprocess

# setting the GPIO mode
GPIO.setmode(GPIO.BCM)


# global variables
SLEEP = 0.3 #Sleep time when a button is pressed
SCAN_PATH = "/home/pi/ScanScripts/"
SYSTEM_PATH = "/home/pi/SystemScripts/"
SHUTDOWN_BUTTON = 17
FAST_BUTTON = 18
COMPLETE_BUTTON = 27


#Setting up the components
GPIO.setup (SHUTDOWN_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP) #Shutdown button
GPIO.setup (FAST_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP) # fast scan button
GPIO.setup (COMPLETE_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP) # complete scan button

# defining processes to avoid a "not defined error"
fast_process = 0
complete_process = 0

#lighting the ready led
scanning_process = subprocess.Popen(["python3",SYSTEM_PATH+"scanning_led.py"])
scanning_process.terminate()
ready_process = subprocess.Popen(["python3", SYSTEM_PATH+"ready_led.py"])

# Main loop
while True:

	# Getting the states of all buttons
	state_shutdown = GPIO.input(SHUTDOWN_BUTTON)
	state_fast = GPIO.input(FAST_BUTTON)
	state_complete = GPIO.input(COMPLETE_BUTTON)

	# checking what action should be made
	if state_shutdown == False:
		ready_process.terminate()
		scanning_process.terminate()
		subprocess.Popen(["python3", SYSTEM_PATH+"off_led.py"]) # red led shortly 
		sleep(3)
		subprocess.Popen(["python3", SYSTEM_PATH+"shutdown.py"])
		sleep(SLEEP)

	if (fast_process == 0 and complete_process == 0) or (fast_process == 0 and complete_process != 0 and complete_process.poll() != None) or (fast_process != 0 and complete_process == 0 and fast_process.poll() != None) or (fast_process != 0 and complete_process != 0 and fast_process.poll() != None and complete_process.poll() != None):

		scanning_process.terminate()
		ready_process = subprocess.Popen(["python3", SYSTEM_PATH+"ready_led.py"])

		if state_fast == False:
			ready_process.terminate()
			fast_process = subprocess.Popen(["python3",SCAN_PATH+"fastScan.py"])
			sleep(SLEEP)

		if state_complete == False:
			ready_process.terminate()
			complete_process = subprocess.Popen(["python3", SCAN_PATH+"completeScan.py"])
			sleep(SLEEP)

	else: # if a scan process is running, blinking green led
		ready_process.terminate()
		if (scanning_process.poll() != None):
			scanning_process = subprocess.Popen(["python3",SYSTEM_PATH+"scanning_led.py"])