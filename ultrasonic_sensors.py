import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigger=18
echo=24

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(trigger, True)
    time.sleep(0.0001)
    GPIO.output(trigger, False)

    start_time=time.time()
    stop_time=time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()

    while GPIO.input(echo) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300)/2

    return distance


while True:
    dist = distance()
    print("Measured Distance =",dist,"cm")
    time.sleep(1)
