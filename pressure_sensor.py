import RPi.GPIO as GPIO
import time
import led

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)

stepped = False

def sensing():
	if  GPIO.input(27) == stepped:
		print ("detected pressure")
		print ("")
		#指定時間だけLED光らせる
		led.led_on("red")
		time.sleep(1.5)
		return True
	
	return False
		



