import time
from gpiozero import LED
led1 = LED(7)
led2 = LED(22)
led3 = LED(23)
number=0

while True:
        time.sleep(0.2)
        if number<=100:
            led1.off()
            led2.on()
            led3.on()
        elif number>201 and number<=300:
            led1.on()
            led2.off()
            led3.on()
        elif number>101 and number<=200:
            led1.on()
            led2.on()
            led3.off()
            
        number=number+1