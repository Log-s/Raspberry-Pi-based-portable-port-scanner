import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)

GPIO.output(22,GPIO.LOW)
GPIO.output(22,GPIO.HIGH)
sleep(2)
GPIO.output(22,GPIO.LOW)