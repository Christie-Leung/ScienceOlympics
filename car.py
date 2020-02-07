'''
Title: Autonomous car
Authors: Abrar Zahin, Christie Leung
Date: 2020/02/05
'''
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

##-- setting up wheels
flWheel = 11 # front left wheel
frWheel = 12 # front right wheel
blWheel = 15 # back left wheel
brWheel = 16 # back right wheel

gpio.setup(flWheel, gpio.OUT)
gpio.setup(frWheel, gpio.OUT)
gpio.setup(blWheel, gpio.OUT)
gpio.setup(brWheel, gpio.OUT)