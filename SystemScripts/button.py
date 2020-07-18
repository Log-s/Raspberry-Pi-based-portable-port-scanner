import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SLEEP = 0.2
BUTTON_PIN = 17


GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

exit = 6

while True:
	state = GPIO.input(BUTTON_PIN)

	if exit == 0:
		break

	if state == False:
		exit -= 1
		print("Pressed ! "+str(exit)+" times left")
		sleep(SLEEP)

print ("\n Bye Bye !")
