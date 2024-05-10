import RPi.GPIO as GPIO

led=14

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pwm_led = GPIO.PWM(led,500)
pwm_led.start(100)

while True:
    duty=int(input("Enter Brightness:"))
    pwm_led.ChangeDutyCycle(duty)
