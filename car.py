'''
Title: Autonomous car
Authors: Abrar Zahin, Christie Leung
Date: 2020/02/05
'''
import RPi.GPIO as gpio
import time

def init(): # initializing method
    gpio.setmode(gpio.BOARD)

    ##-- wheels
    gpio.setup(flWheel, gpio.OUT)
    gpio.setup(frWheel, gpio.OUT)
    gpio.setup(blWheel, gpio.OUT)
    gpio.setup(brWheel, gpio.OUT)

    ##-- distance sensor
    gpio.setup(trig, gpio.OUT)
    gpio.setup(echo, gpio.IN)

    ##-- button
    gpio.setup(button, gpio.IN, pull_up_down = gpio.PUD_UP)

    ##== line sensor
    gpio.setup(lineL, gpio.IN)
    gpio.setup(lineM, gpio.IN)
    gpio.setup(lineR, gpio.IN)

##--== Motor Control code ==--##
def forward():
    gpio.output(flWheel, gpio.HIGH) # forward is high
    gpio.output(blWheel, gpio.LOW) # backward is low
    gpio.output(frWheel, gpio.HIGH)
    gpio.output(brWheel, gpio.LOW)

def leftTurnFront():
    gpio.output(frWheel, gpio.HIGH)
    gpio.output(brWheel, gpio.LOW)

def rightTurnFront():
    gpio.output(flWheel, gpio.HIGH)
    gpio.output(blWheel, gpio.LOW)

##--== Distance Sensor code ==--##
def distance(speed):
    gpio.output(trig, False)

    while gpio.input(echo) == 0:
        noSig = time.time()
    while gpio.input(echo) == 1:
        sig = time.time
    
    gpio.cleanup()
    dist = (sig - noSig)/0.000058

    # keeping a distance of 13cm to 15cm at all times
    if dist < 13:
        speed -= 2
        if speed < 0:
            speed = 0
    elif dist > 15:
        speed += 2
        if speed > 100:
            speed = 100
    else:
        speed = speed
    return speed

##--== Button code ==--##
def mode(m):
    if gpio.input(button) == False and m == 0:
        m += 1
        time.sleep(0.7)
        if m > 1:
            m = 0
    return m

##--== Line Sensor code ==--##
def auto(m):
    if gpio.input(lineL) == 0 and gpio.input(lineM) == 0 and gpio.input(lineR) == 0:
        forward()
        if gpio.input(lineL) == 0 and gpio.input(lineM) == 0 and gpio.input(lineR) == 0:
            m = 0
    if gpio.input(lineL) == 0 and gpio.input(lineM) == 1 and gpio.input(lineR) == 0:
        forward()
    if gpio.input(lineL) == 1 and gpio.input(lineR) == 0:
        leftTurnFront()
    if gpio.input(lineL) == 0 and gpio.input(lineR) == 1:
        rightTurnFront()
    if gpio.input(lineL) == 1 and gpio.input(lineM) == 1 and gpio.input(lineR) == 1:
        m = 0

##--== Variables ==--##
# GPIO pins
flWheel = 11 # forward left wheels
frWheel = 12 # forward right wheels
blWheel = 15 # backward left wheels
brWheel = 16 # backward right wheels
trig = 38 # trig pin in the distance sensor
echo = 40 # echo pin in the distance sensor
button = 7 # button input pin
lineL = 29 # left line sensor
lineM = 31 # middle line sensor
lineR = 33 # right line sensor

init()

# wheel speed control
fl = gpio.PWM(flWheel, 100)
fr = gpio.PWM(frWheel, 100)
bl = gpio.PWM(blWheel, 100)
br = gpio.PWM(brWheel, 100)

m = 0 # m for mode 0 is nothing 1 is auto
speed = 0 # speed in % of the max speed

fl.start(speed)
fr.start(speed)
bl.start(speed)
br.start(speed)

'''
##--== Running the code ==--##
while True:
    try:
        init()
        mode(m)
        if m == 0:
            speed = 0
            fl.ChangeDutyCycle(speed)
            fr.ChangeDutyCycle(speed)
            bl.ChangeDutyCycle(speed)
            br.ChangeDutyCycle(speed)
        else:
            speed = distance(speed)
            fl.ChangeDutyCycle(speed)
            fr.ChangeDutyCycle(speed)
            bl.ChangeDutyCycle(speed)
            br.ChangeDutyCycle(speed)
            auto(m)
        gpio.cleanup()
    finally:
        gpio.cleanup()
    '''

while True:
    try:
        gpio.setmode(gpio.BOARD)
        gpio.setup(button, gpio.IN, pull_up_down = gpio.PUD_UP)
        if gpio.input(button) == False:
            print('beep')
            time.sleep(0.7)
    finally:
        gpio.cleanup()