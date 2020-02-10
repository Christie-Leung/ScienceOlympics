'''
Title: Autonomous car
Authors: Abrar Zahin, Christie Leung
Date: 2020/02/05
'''
import RPi.GPIO as gpio
import time

# Wheel pins
flWheel = 11 # front left wheel
frWheel = 12 # front right wheel
blWheel = 15 # back left wheel
brWheel = 16 # back right wheel

def init(): # initializing method
    gpio.setmode(gpio.BOARD)

    ##-- setting up wheels
    gpio.setup(flWheel, gpio.OUT)
    gpio.setup(frWheel, gpio.OUT)
    gpio.setup(blWheel, gpio.OUT)
    gpio.setup(brWheel, gpio.OUT)

##--== Motor Control code ==--##
def forward():
    gpio.output(flWheel, True)
    gpio.output(frWheel, False)
    gpio.output(blWheel, True)
    gpio.output(brWheel, False)

def leftTurnFront():
    gpio.output(frWheel, False)
    gpio.output(brWheel, False)

def rightTurnFront():
    gpio.output(flWheel, True)
    gpio.output(blWheel, True)

def backward():
    gpio.output(flWheel, False)
    gpio.output(frWheel, True)
    gpio.output(blWheel, False)
    gpio.output(brWheel, True)

def leftTurnBack():
    gpio.output(frWheel, True)
    gpio.output(brWheel, True)

def rightTurnBack():
    gpio.output(flWheel, False)
    gpio.output(blWheel, False)

def leftPivot():
    gpio.output(flWheel, False)
    gpio.output(frWheel, False)
    gpio.output(blWheel, False)
    gpio.output(brWheel, False)

def rightPivot():
    gpio.output(flWheel, True)
    gpio.output(frWheel, True)
    gpio.output(blWheel, True)
    gpio.output(brWheel, True)