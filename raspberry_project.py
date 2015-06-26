import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup (20, GPIO.IN)
GPIO.setup (21, GPIO.OUT)  # red
GPIO.setup (16, GPIO.OUT)  # yellow
GPIO.setup (19, GPIO.OUT)  # green

count = 0
isReleased = True 

motor = GPIO.PWM(17,50)

motor.start(0)
            
while True:
	inputValue = GPIO.input(20)
	if (inputValue == True and isReleased == True):
		count = count+1
		print("Button Pressed " + str(count) + " times.")
		isReleased = False
		
                try:
                    motor.ChangeDutyCycle(5)
                    GPIO.output(21, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(21, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(16, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(16, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(19, GPIO.HIGH)
                    time.sleep(0.5)
                    
                except KeyboardInterrupt:   
                    GPIO.cleanup()

	if(inputValue == False and isReleased == False):
		isReleased = True
		
                try:
                    motor.ChangeDutyCycle(12.5)
                    GPIO.output(19, GPIO.LOW)
                    time.sleep(1)
                    
                    
                except KeyboardInterrupt:
                    GPIO.cleanup()


	time.sleep(0.01)	
