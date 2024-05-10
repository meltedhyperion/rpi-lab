import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led=14
GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, True)
    time.sleep(1)
    GPIO.output(led, False)
    time.sleep(1)
