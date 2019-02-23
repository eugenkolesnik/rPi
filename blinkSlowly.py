import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD numbering schemes. I use BCM
GPIO.setup(7, GPIO.OUT) # set GPIO 26 as output for led
led= GPIO.PWM(7,100)   # create object led for PWM on port 25 at 100 Hertz
led.start(0)            # start led on 0 percent duty cycle (off)
pause_time = 0.02       # you can change this to slow down/speed up

try:
    while True:
        for i in range(0,101):          # 101 because it stops when it finishes 100
            led.ChangeDutyCycle(i)
            time.sleep(pause_time)
        for i in range(100,-1,-1):      # from 100 to zero in steps of -1
            led.ChangeDutyCycle(i)
            time.sleep(pause_time)

except KeyboardInterrupt:
    led.stop()            # stop the led PWM output
    GPIO.cleanup()        # clean up GPIO on CTRL+C exit
