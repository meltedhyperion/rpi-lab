import RPi.GPIO as GPIO
import time

INPUT_PIN=18
OUTPUT_PIN=23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)

while True:
    button_state = GPIO.input(INPUT_PIN)
    if button_state == False:
        GPIO.output(OUTPUT_PIN, True)
        time.sleep(0.5)
    else:
        GPIO.output(OUTPUT_PIN, False)
