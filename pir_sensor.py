import RPi.GPIO as GPIO
impirt time

PIR_PIN=29
LED_PIN=32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT) 

try:
    print("PIR Module Test (Ctrl+C to exit)")
    time.sleep(2)
    print("Ready")

    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected")
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(1)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1.0)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
