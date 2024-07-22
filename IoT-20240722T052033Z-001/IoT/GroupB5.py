import time
from gpiozero import LED

led1 = LED(7)
led2 = LED(22)
led3 = LED(23)
led4 = LED(25)

while True:
	try:
		led1.off()
		time.sleep(0.5)
		led1.on()
		led2.off()
		time.sleep(0.5)
		led2.on()
		led3.off()
		time.sleep(0.5)
		led3.on()
		led4.off()
		time.sleep(0.5)
		led4.on()
		time.sleep(0.5)
		
	except KeyboardInterrupt:
		print("closing")	
		exit()