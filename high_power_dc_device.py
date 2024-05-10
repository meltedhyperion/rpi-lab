import RPi.GPIO as GPIO          
import sleep from time                           

relay=12       

GPIO.setwarnings(False)          
GPIO.setmode(GPIO.BOARD)         
GPIO.setup(relay, GPIO.OUT)      

for i in range(4):               
    GPIO.output(relay, GPIO.LOW) 
    sleep(1)   
    GPIO.output(relay, GPIO.HIGH)
    sleep(1)                  

GPIO.cleanup()
