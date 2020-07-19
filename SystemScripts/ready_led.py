#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22,GPIO.OUT)

GPIO.output(22,GPIO.LOW)
GPIO.output(22,GPIO.HIGH)