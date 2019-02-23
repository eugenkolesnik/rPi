import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

dot = 0.2
dash =  dot*3
gap = dot*7

def blinkShort ():
    GPIO.output(7, 1)
    time.sleep(dot)
    GPIO.output(7, 0)
    return;

def blinkLong ():
    GPIO.output(7, 1)
    time.sleep(dash)
    GPIO.output(7, 0)
    return;

def blinkS ():
    blinkShort()
    time.sleep(dot)
    blinkShort()
    time.sleep(dot)
    blinkShort()
    return;

def blinkO ():
    blinkLong()
    time.sleep(dot)
    blinkLong()
    time.sleep(dot)
    blinkLong()
    return;

def blinkSOS():
    blinkS()
    time.sleep(dash)
    blinkO()
    time.sleep(dash)
    blinkS()
    return;

try:
    while True:
        blinkSOS()
        time.sleep(gap)

except KeyboardInterrupt:
    GPIO.output(7, 0)
    GPIO.cleanup()
