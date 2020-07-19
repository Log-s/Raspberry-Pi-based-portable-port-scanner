#! /usr/bin/python3

import RPi.GPIO as GPIO
import sys
from time import sleep

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#variables
A = 19
B = 26
C = 20
D = 16
E = 12
F = 13
G = 6
DOT = 21

pins = [A, B, C, D, E, F, G, DOT]

digit = {
    0 : (0,0,0,0,0,0,1,0),
    1 : (1,0,0,1,1,1,1,0),
    2 : (0,0,1,0,0,1,0,0),
    3 : (0,0,0,0,1,1,0,0),
    4 : (1,0,0,1,1,0,0,0),
    5 : (0,1,0,0,1,0,0,0),
    6 : (0,1,0,0,0,0,0,0),
    7 : (0,0,0,1,1,1,1,0),
    8 : (0,0,0,0,0,0,0,0),
    9 : (0,0,0,0,1,0,0,0),
    "p" : (0,0,1,1,0,0,0,1),
    "o" : (1,1,1,1,1,1,1,1)
}

NUMBER = int(sys.argv[1])
if NUMBER > 9:
    NUMBER = "p" # if the number is greater than 9, display p for "plus"
elif NUMBER < 0:
    NUMBER = "o" # if a negative value is given, turns everything off

#setting up ports
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# displaying the number
for i, pin in enumerate(pins):
    GPIO.output(pin, digit.get(NUMBER)[i])