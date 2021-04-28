#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

# GPIO initialization
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)

# set pins to variables
in1 = 7
in2 = 8
in3 = 9
in4 = 10
ena = 13
enb = 12

# set GPIO pin mode
# left side
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

# right side
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

# set initial state to off
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

# configure HW PWM
p1=GPIO.PWM(ena,1000)
p2=GPIO.PWM(enb,1000)

p1.start(100)
p2.start(100)

# turn right motor forward
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.LOW)

# turn left motor forward
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)

time.sleep(1)

# reset GPIO and turn off motors
GPIO.cleanup()