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
SHUTDOWN_BUTTON = 17
FAST_BUTTON = 18
COMPLETE_BUTTON = 27


#Setting up the components
GPIO.setup (SHUTDOWN_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP) #Shutdown button
GPIO.setup (FAST_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP) # fast scan button

# Main loop
while True:

	# Getting the states of all buttons
	state_shutdown = GPIO.input(SHUTDOWN_BUTTON)
	state_fast = GPIO.input(FAST_BUTTON)
	state_complete = GPIO.input(COMPLETE_BUTTON)

	# defining processes to avoid a "not defined error"
	fast_process = 0
	complete_process = 0

	# checking what action should be made
	if state_shutdown == False:
		print ("Exiting...")
		subprocess.Popen(["python3","off_led.py"]) # red led shortly 
		sleep(3)
		subprocess.Popen(["python3","shutdown.py"])
		sleep(SLEEP)

	if fast_process != None and complete_process != None: # if no scan process is running

		# if no scan process is running, green led is light
		subprocess.Popen(["python3","ready_led.py"])

		if state_fast == False:
			print ("Fast scan")
			fast_process = subprocess.Popen(["python3","/home/pi/ScanScripts/fastScan.py"])
			sleep(SLEEP)

		if state_complete == False:
			print ("Complete scan")
			complete_process = subprocess.Popen(["python3","/home/pi/ScanScripts/completeScan.py"])
			sleep(SLEEP)

	else: # if a scan process is running, blinking green led
		subprocess.Popen(["python3","scanning_led.py"])
		sleep(1)