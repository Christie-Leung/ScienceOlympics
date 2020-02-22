'''
bs
'''
import RPi.GPIO as gpio
import time

def forward(tf):
    gpio.setmode(gpio.BOARD)
    
    gpio.setup(11, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)

    gpio.output(11, True)
    gpio.output(12, False)
    gpio.output(15, True)
    gpio.output(16, False)
    time.sleep(tf)

    gpio.cleanup()

def turnLeft(tf):
    gpio.setmode(gpio.BOARD)
    
    gpio.setup(11, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)

    gpio.output(11, True)
    gpio.output(12, True)
    time.sleep(tf)

    gpio.cleanup()

def turnRight(tf):
    gpio.setmode(gpio.BOARD)
    
    gpio.setup(11, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)

    gpio.output(12, False)
    gpio.output(15, False)
    time.sleep(tf)

    gpio.cleanup()

def button(m):
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.IN, pull_up_down = gpio.PUD_UP)

    if gpio.input(7) == False:
        m += 1
        time.sleep(0.5)
        if m > 1:
            m = 0
    
    gpio.cleanup()
    return m

def getDistance():
    gpio.setmode(gpio.BOARD)

    gpio.setup(40, gpio.OUT)
    gpio.setup(38, gpio.IN)

    gpio.output(40, False)
    gpio.output(40, True)
    time.sleep(0.00001)
    gpio.output(40, False)

    while gpio.input(38) == False:
        start = time.time()

    while gpio.input(38) == True:
        end = time.time()

    gpio.cleanup()
    dist = (end - start)/0.000058
    return dist

def line():
    gpio.setmode(gpio.BOARD)

    gpio.setup(29, gpio.IN) #purple
    gpio.setup(31, gpio.IN) #green
    gpio.setup(33, gpio.IN) #blue

    l, m, r = gpio.input(33), gpio.input(31), gpio.input(29)
    gpio.cleanup()
    return l, m, r

def automatic(tf, md, n):
    l, m, r = line()

    if l == 1:
        n = 0
        turnLeft(tf)
    if r == 1:
        n = 0
        turnRight(tf)
    if m == 1:
        n = 0
        forward(tf)
    if l == 0 and m == 0 and r == 0:
        n += 1
        if n >= int(3/tf):
            md = 0
        forward(tf)
    return md, n

timeFrame = 0.03
mode = 0
num = 0

while True:
    try:
        mode = button(mode)

        if mode == 1 and getDistance() >= 20:
            mode, num = automatic(timeFrame, mode, num)
    
        else:
            num = 0
            gpio.setmode(gpio.BOARD)
            gpio.setup(7, gpio.IN, pull_up_down = gpio.PUD_UP)
            gpio.cleanup()

    finally:
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.IN, pull_up_down = gpio.PUD_UP)
        gpio.cleanup()